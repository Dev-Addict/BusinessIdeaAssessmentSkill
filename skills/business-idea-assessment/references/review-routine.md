# Review routine

“Perfect” means no known internal defect remains after repeated review. It does
not mean external facts, demand, approvals, safety, funding, or future outcomes
are certain.

Maintain `review_log.md` with checks, defects, fixes, remaining external gaps,
and the final result.

## Gate 1 — evidence review

Run after competitor, market, regulatory, supplier, program, and cost inputs are
collected but before conclusions depend on them.

Check:

- every consequential claim has a direct supporting source and access date;
- primary sources are used where available;
- observed facts, estimates, assumptions, inferences, and unresolved leads are
  distinguishable;
- current availability, capability, eligibility, and local presence are not
  inferred from generic web pages;
- source dates, currencies, units, and geography are explicit; and
- missing evidence has an owner and practical acquisition method.

Fix defects and rerun this gate before modelling.

## Gate 2 — model and draft review

Run after the initial deliverables are drafted.

Check:

- CSV structure, headers, row widths, stable IDs, dates, and units;
- all formulas, currency conversions, normalized prices, scenario identities,
  cumulative cash, break-even, margins, and sensitivities;
- cross-file agreement on prices, volumes, yield/utilization, margin, capital,
  timing, success definition, and recommended concepts;
- total market versus obtainable sales distinction;
- a numerical probability range for every success-matrix row and prominently
  for the recommended route, with numeric bounds from 0 through 100 and lower
  not greater than upper;
- reference class, assumptions, contrary evidence, confidence, and material
  range-moving evidence documented without invented customer data;
- unsupported precision, invented survey data, omitted numerical estimates,
  and probabilities presented as observed or statistically measured when they
  are judgmental;
- legal/safety/technical statements for scope and appropriate caveats; and
- README coverage and local-link resolution.

Repair the model and every downstream conclusion affected by a correction, then
rerun both Gates 1 and 2.

## Gate 3 — autonomous-work integration review

Run after `next_steps/` work is complete.

Check:

- follow-on artifacts implement the initial recommendation and gates;
- action, cash, 30/60/90-day, funding, and test budgets reconcile;
- contact, supplier, task, claim, and decision IDs resolve across files;
- drafts do not claim they were sent, accepted, tested, or approved;
- proposed tests cannot run before their compliance/safety dependencies;
- old assumptions remain traceable when quote or measured ranges are added; and
- both READMEs link every new deliverable.

Fix and rerun Gate 3 plus any earlier gate affected by the change.

## Gate 4 — final clean-room review

Review the entire package as if encountering it for the first time.

1. Run `scripts/validate_assessment.py`.
2. Recalculate high-impact rows independently from their written formulas.
3. Trace the executive recommendation backward to sources and assumptions.
4. Search for overclaims: `guaranteed`, `approved`, `safe`, `available locally`,
   `proven demand`, fixed shelf life, probabilities described as measured facts,
   and similar language. Also search for a missing numerical probability range.
5. Confirm every unresolved external fact is still labelled and routed.
6. Make fixes and rerun until a complete pass finds no new internal defect.

Record the exact final scope and counts. If a source is inaccessible, preserve
the gap and confidence level rather than silently dropping or upgrading it.

