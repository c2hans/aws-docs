---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/compile-time-hardening.html
---

# Compile-time hardening
<a name="compile-time-hardening"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

With AL2027, all C and C\+\+ packages are compiled with a set of hardening flags that reduce common classes of defects at build time. You don't need to take any action to benefit from these flags. They're active in every package that supports them.

## Hardening flags
<a name="hardening-flags-new"></a>

With AL2027, you get four compile-time hardening flags for C and C\+\+ packages. Each flag stops the compiler from applying an optimization that can turn a latent source-level defect into a runtime problem. Some flags also make undefined behavior deterministic. The following sections describe each flag and what it does.

`-ftrivial-auto-var-init=zero`
**Prevents: use of uninitialized stack memory.** Zeroes all stack-allocated variables (local variables not explicitly initialized). Without this flag, such a variable holds whatever data was previously stored at that stack location. Reading an uninitialized variable before assignment yields undefined data. Zero-initialization makes that behavior deterministic and removes a class of information-disclosure and uninitialized-pointer defects.

`-fno-delete-null-pointer-checks`
**Preserves: explicit NULL checks.** By default, when the compiler sees a pointer dereference followed by a NULL check, it may conclude the pointer cannot be NULL and remove the later check as redundant. This flag keeps such checks in place, so defensive code behaves as written.

`-fno-strict-overflow`
**Preserves: signed integer overflow checks.** The C standard treats signed integer overflow as undefined behavior, which allows the compiler to assume it never happens and to remove checks such as `if (x + 1 < x)` as unreachable. This flag preserves these checks as written in the source, so they evaluate as intended.

`-fno-strict-aliasing`
**Relaxes: type-based aliasing assumptions.** C's strict aliasing rules let the compiler assume that pointers of different types do not refer to the same memory, and reorder or eliminate loads and stores on that basis. This flag disables those assumptions, so such code compiles to what the source expresses.

## Overriding hardening flags
<a name="hardening-flags-override"></a>

You can override specific hardening flags for your own packages in their RPM spec file when necessary — for example, if a flag is incompatible with your build toolchain or introduces a performance regression. If you build your own RPM packages on AL2027, the hardening flags are applied automatically through the `amazon-rpm-config` macros. To check whether a specific flag is active in your build, inspect the compiler command lines in the build log.
