---
source_url: https://docs.aws.amazon.com/continuum/latest/userguide/code-vulnerabilities.html
---

# Code vulnerabilities

AWS Continuum for code vulnerabilities is a feature of AWS Continuum that discovers, validates, prioritizes, and recommends remediation for code vulnerabilities.

AWS Continuum for code vulnerabilities integrates with GitHub, GitLab, and Amazon S3 for code and context. You connect a code source, add context about your infrastructure and business, and then review the issues and patches that AWS Continuum produces.

AWS Continuum tracks generated GitHub pull requests and GitLab merge requests as open, merged, or closed without merging. After all requests for an issue's latest remediation run merge into their original target branches, AWS Continuum closes the issue to new findings. If a later finding identifies the vulnerability again, it can start a new issue and remediation attempt. For details, see [Tracking pull and merge requests](cv-viewing-patches.md#cv-viewing-patches-lifecycle).

**Topics**
+ [Supported languages and source files](cv-supported-languages.md)
+ [Getting started with code vulnerabilities](cv-getting-started.md)
+ [Adding AWS context](cv-adding-context.md)
+ [Connecting an Amazon EKS cluster to AWS Continuum](cv-onboard-eks-cluster.md)
+ [Triggering a scan](cv-triggering-scan.md)
+ [Controlling which findings AWS Continuum pursues](cv-focus-mode-issue-budget.md)
+ [Viewing discovered issues](cv-viewing-issues.md)
+ [Viewing generated patches](cv-viewing-patches.md)
