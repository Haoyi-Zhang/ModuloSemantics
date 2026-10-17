# Literature sources and reading scope

`reference-audit.json` and its CSV counterpart describe the 50 references cited
by the manuscript. Publication identity and technical claim support are separate:
the DOI, title and venue identify a work; `current_claims` maps the manuscript's
citation sentences to original passages, their premises and their reading scope.
`claim_support_status` summarizes those mappings, not the existence of a matching
DOI. Source-version and pagination notes distinguish publisher copies, author
manuscripts, reports and reconstructions.

Four supplied originals were read completely, with their figures and tables
inspected: Leothaud et al., DAC 2025 (7 pages); Leothaud et al., DATE 2026
(7 pages); EagerlyElastic, FPGA 2026 (11 pages); and She et al., TRETS 2025
(33 pages). Only these four entries set `entire_fulltext_read_claim` to true.
Other entries distinguish selected body passages, official primary abstracts
and unresolved full-body access. Five bounded background attributions use primary
abstracts rather than article bodies. All 50 keys have support for their current
bounded citation claims. A supported background statement does not certify an
entire paper, its implementation or all dependencies of its proofs.

Rau's allocation-scope attribution uses the ACM-deposited original abstract for
the SIGPLAN Notices companion publication, DOI 10.1145/143103.143141, with the
same title, four authors, year and pages as the cited proceedings work. The
conference DOI 10.1145/143095.143141 is retained. The abstract distinguishes
targets with and without specialized hardware; the jointly cited spill-paper
bodies supply the broader residence/transfer choices. Rau's full article body
remains unread and is not credited.

The comparisons concern width-weighted rollback placement, unpipelining and
resource sharing, context-dependent elastic rewrites, and iterative recurrence-
path modeling with committed inter-component FIFOs. ModuloSemantics fixes operation
placements, latencies and resource reservations while choosing Ret/Forward
annotations and export times for separate uniform tagged forwarding banks.
The scientific comparison is summarized in
[`../proofs/literature.md`](../proofs/literature.md).

`access-boundaries.json` retains unsuccessful endpoint observations and records
their current resolution. A failed endpoint is not evidence that a mechanism is
absent, and later access does not erase the earlier observation. The historical
DAC presentation remains supplementary evidence, not a substitute for the paper.
`../external_resources.csv` retains the existing external-resource inventory;
the 50-reference ledger gives the per-citation reading scope.

Third-party papers, slides, figures and implementations are not bundled here.
Public availability does not grant redistribution permission. Existing template
licenses and resource notices remain applicable. No source hardware speedup or
area measurement is used as a measurement of this artifact's abstract periods
or forwarding-cell counts.
