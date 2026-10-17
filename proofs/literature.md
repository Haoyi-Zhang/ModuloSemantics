# Scientific comparison with related work

ModuloSemantics separates a source-correct private value-or-fault export from source-ordered
public retirement. Its optimization fixes source identities and dependence
distances, operation placements, latencies, releases and resource reservations.
It chooses carried Ret/Forward annotations and fixed export times, minimizing
separate uniform iteration-tagged forwarding banks. The inclusive lifetime count
uses export-before-read event order and the labelled reservation envelope, not
all target registers or physical area.

| Source | Original technical passages | Comparison with ModuloSemantics |
|---|---|---|
| Tristan and Leroy, POPL 2010, DOI 10.1145/1706299.1706311 | Section 4 encountered computations; Sections 5-6.1 bounded equations and arbitrary-bound unrolled-loop correctness; Section 6.2 CFG extension and proof status. Physical pp. 4, 6-7. | Failure-sensitive validation and arbitrary-loop-bound reasoning are established context. ModuloSemantics supplies a different timed ticket/export relation; its handwritten proof and finite checker do not inherit the source's Coq assurance. |
| Herklotz and Wickerson, PLDI 2024, DOI 10.1145/3656455 | Sections 5 and 6.4-6.5; predicated summaries, encountered expressions, constructor/validator distinction and future modulo scheduling. Physical pp. 2, 8, 13-14. | Predicated validation can account for encountered computations that fail. ModuloSemantics's predicates are exogenous inputs with declared releases; its periodic causal-selector and bank objective keep those premises explicit. |
| Leothaud et al., DAC 2025, DOI 10.1109/DAC63849.2025.11133015 | Sections III-A/D, physical pp. 3-5; Figures 4-7. | Reversibility, speculative-gamma postdominance and constrained, bit-width-weighted retiming simplify or relocate rollback state. ModuloSemantics changes carried annotations and export times on fixed placements; a forwarding-cell objective is not the rollback-register or hardware-area objective. |
| Leothaud et al., DATE 2026, DOI 10.23919/DATE69613.2026.11539349 | Section III and III-C/E, physical pp. 2-5; Figures 3-6; Section V, p. 6. | Unpipelining separately schedules a speculative core and recovery work, using mutual exclusion for resource sharing and speculative array partitioning. Its deterministic fallback can stall the pipeline. ModuloSemantics retains supplied reservations and does not repair a capacity violation by stalling. |
| EagerlyElastic, FPGA 2026, DOI 10.1145/3748173.3779196 | Sections 3.5 and 4.1-4.5, physical pp. 5-7 (printed 107-109); Figures 3-5; Sections 5-6, p. 8. | Context-dependent rewrites verified with ElasticMiter move suppressors, permit eager paths and repeated loop re-entry, and retain computational units. Delayed commitment and unchanged computational units are genuine overlap, not ModuloSemantics's differentiator. The fixed timed value-or-fault interface and separate-bank objective specify ModuloSemantics's problem. |
| She et al., TRETS 2025, DOI 10.1145/3705732 | Section 4.2, physical pp. 11-12; Section 5.1, pp. 12-14; Section 5.4, pp. 16-18; Figures 3-4 and 6. | ASLP tunes transformed recurrence paths through backend synthesis, analyzes storage overhead from overestimation and connects separately synthesized components with FIFOs. Within-component speculative recurrences can require rollback/replay; inter-component outputs enter the FIFO only after commitment. ModuloSemantics exports already-correct denotations without later repair before public retirement. |

Instruction scheduling, lifetime-sensitive placement, register allocation,
spilling and elastic-network buffering consider related but different choices.
The per-source ledger gives the selected formulations and their assumptions.
In particular, separate uniform banks exclude shared allocation, spilling and
rematerialization; fixed offsets exclude moving instructions to shorten live
ranges; the unconditional labelled envelope differs from backpressured FIFO
occupancy. These distinctions specify the admitted optimization domain.

The observation theorem preserves the emission trace, last-value map and first
defined source fault in the stated lifted, deterministic language. A trapping
instruction, irreversible store or concurrent memory system needs its own
semantic mapping. Source hardware evaluations use different implementations and
costs and are not measurements of ModuloSemantics. Reproducing the artifact's finite tests
requires no external paper or implementation.

Detailed source versions, exact current citation sentences, locators, reading
scope and remaining proof/implementation limits are recorded in
[`../literature/reference-audit.json`](../literature/reference-audit.json).
Third-party texts and figures are not redistributed.
