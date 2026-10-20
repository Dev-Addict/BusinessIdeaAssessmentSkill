# Deliverable contract

Use this file when generating a full assessment. Preserve auditability over a
fixed filename when the business model calls for a clearer term.

## Required core package

- `README.md` — navigation, date, jurisdiction, currency, key findings,
  executive recommendation, next gate, and limitations.
- `opportunity_definition.md` and `opportunity_comparison.csv`
- `competitors_and_substitutes.md` and `competitor_offers.csv`
- `market_and_channels.md` and `channel_comparison.csv`
- `feasibility_and_compliance.md`
- `operations_and_costs.md`
- `unit_economics.csv` and `financial_scenarios.csv`
- `success_matrix.md` and `success_matrix.csv`
- `funding_and_support.md` and `funding_programs.csv`
- `risk_register.md` and `risk_register.csv`
- `routes_to_market.md`
- `assumptions_and_sources.md`

Add domain-specific files where they improve a decision—for example technical
validation, data/privacy, intellectual property, procurement, site selection,
or safety. Do not create empty deliverables for inapplicable topics; explain the
exclusion in the README.

## CSV design rules

- Use stable row IDs where records will be referenced elsewhere.
- Put units in headers: `_cad`, `_cad_per_unit`, `_kg`, `_hours`, `_pct`.
- Give each numeric column one unit. Do not mix monthly and annual values.
- Use ISO dates (`YYYY-MM-DD`) and direct source URLs.
- Use `NA` for unavailable data, not zero. Zero means observed or assumed zero.
- Include status/confidence columns where records mix verified facts and leads.
- Quote fields containing commas or line breaks.

## Minimum formula documentation

Document the applicable formulas in `operations_and_costs.md` or
`success_matrix.md` and make every CSV reconcile to them. Typical identities:

```text
normalized_price = observed_price × currency_conversion ÷ comparable_quantity
revenue = paid_units × realized_net_revenue_per_unit
gross_profit = revenue - cost_of_goods_or_service_delivery
contribution = gross_profit - channel_variable_cost
operating_profit_before_founders = contribution - operating_cost
profit_after_founders = operating_profit_before_founders - founder_compensation
cash_flow = profit_after_founders - capital_expenditure - working_capital_change
break_even_units = fixed_cost ÷ contribution_per_unit
```

Use the correct formula for the model; do not force product terminology onto a
service, software, marketplace, or licensing business.

## Claim and source discipline

Put a direct URL and access/observation date beside material external claims.
When one source supports only part of a row, state the boundary. Examples:

- A facility advertises packaging: packaging is verified; capability for the
  proposed material/process remains `to_confirm`.
- A retailer lists a product online: the listing and observed price are
  verified; local inventory and sales velocity are not.
- A program page is current: program existence is verified; applicant
  eligibility and award are not.

## README completeness

Link every deliverable directly from the root README. Readers should not need to
search the directory. State which numbers are assumptions, the decision date,
and how to replace estimates with observed evidence without erasing history.

