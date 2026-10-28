"""The `shopkit` command."""

from __future__ import annotations

import argparse
import sys

from shopkit.cart import Cart
from shopkit.catalog import list_products, search_products
from shopkit.money import format_price
from shopkit.pricing import InvalidCouponError


def _print_products(products) -> None:
    for p in products:
        print(f"{p.sku:<10} {p.name:<22} {format_price(p.price):>10}")


def cmd_list(args: argparse.Namespace) -> int:
    _print_products(list_products(args.category))
    return 0


def cmd_search(args: argparse.Namespace) -> int:
    results = search_products(args.query)
    if not results:
        print("No products found.")
        return 1
    _print_products(results)
    return 0


def cmd_quote(args: argparse.Namespace) -> int:
    cart = Cart()
    for line in args.lines:
        sku, _, qty = line.partition(":")
        try:
            cart.add(sku, int(qty or 1))
        except (KeyError, ValueError) as e:
            print(f"error: {e}", file=sys.stderr)
            return 2
    try:
        q = cart.quote(args.coupon)
    except InvalidCouponError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    print(f"Subtotal: {format_price(q.subtotal)}")
    print(f"Discount: -{format_price(q.discount)}")
    print(f"Tax:      {format_price(q.tax)}")
    print(f"Total:    {format_price(q.total)}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="shopkit")
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("list", help="List products.")
    p.add_argument("--category")
    p.set_defaults(func=cmd_list)
    p = sub.add_parser("search", help="Search products by name.")
    p.add_argument("query")
    p.set_defaults(func=cmd_search)
    p = sub.add_parser("quote", help="Price an order of SKU:QUANTITY lines.")
    p.add_argument("lines", nargs="+")
    p.add_argument("--coupon")
    p.set_defaults(func=cmd_quote)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
