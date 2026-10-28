# shopkit

A tiny toolkit for running a small online store: a product catalog, shopping carts, pricing with coupons and bulk discounts, inventory tracking and delivery estimates.

## Usage

List the catalog:

```
shopkit list
shopkit list --category kitchen
```

Search by name:

```
shopkit search mug
```

Price an order (`SKU:QUANTITY`), optionally with a coupon:

```
shopkit quote MUG-BLU:2 TEA-GRN:1 --coupon SAVE10
```

## Pricing rules

- Orders of **10 or more items** get a 5% bulk discount.
- Coupons: `SAVE10` (10% off) and `WELCOME5` (5% off). Codes are not case-sensitive.
- Sales tax is 8%, applied after discounts.

## Shipping

Standard delivery takes 5 business days and express takes 2. Business days are Monday to Friday.

## Development

```
uv run pytest
uv run ruff check .
```
