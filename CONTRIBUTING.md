# Contributing

Contributions that improve decision quality, evidence discipline, model
auditability, or safe autonomy are welcome.

## Before opening a change

1. Keep the skill general across products, services, software, marketplaces,
   regulated businesses, and local operations.
2. Add rules only when they materially change agent decisions or prevent a
   demonstrated failure. Avoid turning one business example into a universal
   workflow.
3. Preserve the boundary between local drafting/research and external actions
   that require user authorization.
4. Do not add private research, personal data, API keys, proprietary formulas,
   or confidential supplier information.
5. Prefer primary sources in any example that makes a factual claim.

## Validate

Run both checks before opening a pull request:

```bash
python3 skills/business-idea-assessment/scripts/validate_repository.py .
python3 skills/business-idea-assessment/scripts/validate_assessment.py --self-test
```

For behavioural changes, walk through the relevant cases in
[tests/behavioral_cases.md](tests/behavioral_cases.md) and describe the observed
result in the pull request.

## Pull requests

Keep changes focused. Explain:

- the user request or failure mode;
- why existing instructions were insufficient;
- the smallest effective change;
- validation performed; and
- any compatibility or safety effect.

By contributing, you agree that your contribution is licensed under the MIT
License used by this repository.

