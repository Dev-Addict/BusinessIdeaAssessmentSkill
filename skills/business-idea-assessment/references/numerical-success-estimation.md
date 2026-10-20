# Numerical success estimation

Read this reference before creating or revising `success_matrix.md` and
`success_matrix.csv`. A completed assessment always includes a numerical
probability range. Sparse evidence changes the width and confidence of the
estimate, not whether an estimate is made.

## 1. Define the event

State exactly what counts as success and by when. Use the user's definition when
provided. Otherwise choose a decision-relevant default, normally sustainable
operating break-even plus explicitly assumed founder compensation by the end of
year 5. Adapt the event for a lifestyle business, venture-scale company,
nonprofit, acquisition target, or other model and state the change.

Do not estimate an undefined outcome such as “the idea works.” The probability
applies only to the stated event, route, starting conditions, and horizon.

## 2. Estimate the right units

Provide a range for every sensible offer × sales-strategy combination in the
success matrix. Also surface the recommended route's range in the executive
README. If an overall company estimate is useful, define how the routes interact
and do not treat dependent alternatives as independent chances.

## 3. Build an evidence hierarchy

Use the strongest available evidence in roughly this order:

1. paid behaviour, repeat purchase, retention, signed orders, or equivalent
   revealed preference;
2. validated technical/regulatory feasibility and supplier capability;
3. verified unit economics, reachable channel performance, and capacity;
4. close reference-class outcomes from credible sources;
5. adjacent business, product, geography, or channel reference classes;
6. transparent assumptions and structured judgment when evidence is absent.

Never invent a base rate, survey result, conversion rate, or cohort. When no
credible quantitative reference class exists, say so and use an explicitly
judgmental range rather than withholding a number.

## 4. Form the range

Use a neutral, repeatable process:

1. Select the closest defensible reference class. Explain its fit and mismatch.
2. Establish a broad starting interval. Cite a source if it supplies a base
   rate; otherwise label the interval an analyst judgment.
3. Assess demand and repeat potential, contribution economics, technical and
   regulatory feasibility, channel access, capital sufficiency, founder
   capacity, competitive response, and timing.
4. Record evidence that raises the range and evidence that lowers it. Missing
   validation is not positive evidence and may represent a material gating risk.
5. Cross-check the range against conservative/base/optimistic financial cases,
   break-even volume, capacity, cash runway, and the risk register.
6. Stress-test the estimate from a sceptical investor, operator, customer, and
   competitor perspective. Correct optimism, novelty, and founder-preference
   bias.
7. Use the same rubric across alternatives, then check that their relative
   ordering matches the evidence and economics.

Do not mechanically multiply arbitrary component scores as if risks were
independent. A calculation is acceptable only when its inputs and dependencies
have a defensible interpretation. Usually an anchored judgment range with a
clear audit trail is more honest.

## 5. Represent uncertainty numerically

For every row, include:

- `subjective_success_probability_low_pct` — numeric lower bound, 0 to 100;
- `subjective_success_probability_high_pct` — numeric upper bound, 0 to 100;
- `confidence` — evidence confidence such as `very_low`, `low`, `medium`, or
  `high`;
- `probability_basis` — concise reference class and adjustment rationale; and
- `key_dependency` — the fact or milestone most capable of changing the range.

The lower bound must not exceed the upper bound. Use whole percentages unless a
more precise value is genuinely justified. Avoid 0% or 100% except when the
defined event is logically impossible or certain under stated conditions.

Wide ranges are appropriate at concept stage. Confidence describes the quality
and coverage of evidence; it is not a substitute for the probability range.

## 6. Explain the estimate

In `success_matrix.md`, document:

- success definition and time horizon;
- numerical range for each combination and the recommended route;
- reference class and why it is imperfect;
- assumptions and observed evidence;
- strongest positive and negative adjustments;
- confidence level and major dependencies;
- evidence that would materially raise or lower the range; and
- date of the estimate.

State plainly that the range is a subjective, evidence-informed planning
estimate, not a measured startup-survival statistic or a promise. This caveat
must accompany the number, not replace it.
