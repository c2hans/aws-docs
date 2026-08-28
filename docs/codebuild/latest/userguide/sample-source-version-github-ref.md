---
source_url: https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version-github-ref.html
---

# Specify a GitHub repository version with a reference and commit ID
<a name="sample-source-version-github-ref"></a>

You can specify a source version with a reference and a commit ID in this format: `{{refs}}/{{heads}}/{{branchname}}^{{{full-commit-SHA}}}` (for example, `refs/heads/main^{12345678901234567890123467890123456789}`). If you do this, CodeBuild downloads only the specified branch to find the version.

**To specify a GitHub repository version with a reference and commit ID.**

1. Complete the steps in [Specify a GitHub repository version with a commit ID](sample-source-version-github.md).

1.  From the left navigation pane, choose **Build projects**, and then choose the project you created earlier.

1.  Choose **Start build**.

1.  In **Source version**, enter **refs/heads/main^{046e8b67481d53bdc86c3f6affdd5d1afae6d369}**. This is the same commit ID and a reference to a branch in the format `{{refs}}/{{heads}}/{{branchname}}^{{{full-commit-SHA}}}`.

1.  Choose **Start build**.

1. When the build is complete, you should see the following:
   +  On the **Build logs** tab, which version of the project source was used. Here is an example.

     ```
     [Container] Date Time Running command echo $CODEBUILD_RESOLVED_SOURCE_VERSION
     046e8b67481d53bdc86c3f6affdd5d1afae6d369

     [Container] Date Time Phase complete: BUILD State: SUCCEEDED
     ```
   +  On the **Environment variables** tab, the **Resolved source version** matches the commit ID used to create the build.
   +  On the **Phase details** tab, the duration of the `DOWNLOAD_SOURCE` phase should be shorter than the duration when you used only the commit ID to specify the version of your source.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
