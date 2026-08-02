---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/troubleshooting-v3-dirs-must-keep.html
---

# Replacing directories
<a name="troubleshooting-v3-dirs-must-keep"></a>

Some directories can't be replaced. If you're having issues replacing the directory, that might be the case. The following directories are shared between the nodes and can't be replaced.
+  `/opt/intel` - This includes Intel MPI, Intel Parallel Studio, and related files.
+  `/opt/slurm` - This includes Slurm Workload Manager and related files. (Conditional, only if `Scheduler: slurm`.)
