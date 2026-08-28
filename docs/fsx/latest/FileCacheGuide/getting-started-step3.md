---
source_url: https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/getting-started-step3.html
---

# Step 3: Run your analysis
<a name="getting-started-step3"></a>

Now that your cache is created and mounted to a compute instance, you can use it to run your high-performance compute workload. The workload loads data from the Amazon S3 data repository as files are accessed by your workload.

After you run the workload, you can export the data that you write to your cache back to your Amazon S3 bucket at any time. From a terminal on one of your compute instances, run the following command to export a file to your Amazon S3 bucket.

```
sudo lfs hsm_archive {{file_name}}
```

For more information about how to run this command on a folder or large collection of files quickly, see [Exporting files using HSM commands](exporting-files-hsm.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
