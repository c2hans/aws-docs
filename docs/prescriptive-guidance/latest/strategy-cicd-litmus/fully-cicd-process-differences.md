---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-cicd-litmus/fully-cicd-process-differences.html
---

# How fully CI/CD processes are different
<a name="fully-cicd-process-differences"></a>

CI/CD pipelines use a modern *trunk-based workflow*, in which developers merge small, frequent updates into a main branch (or *trunk*) that is built and tested through the CD portion of the CI/CD pipeline. This workflow has replaced the *Gitflow workflow*, in which development and release branches are separated by a release schedule. In many organizations, Gitflow is still a popular method of version control and deployment. However, it is now considered legacy, and it can be challenging to integrate into a CI/CD pipeline.

For many organizations, the transition from a Gitflow workflow to a trunk-based workflow has been incomplete, and the result is that they get stuck somewhere along the way and never fully migrate to CI/CD. Somehow, their pipelines end up clinging to certain remnants of the legacy workflow, stuck in a transitional state between past and present. Review the differences in the Git workflows, and then learn how using a legacy workflow can affect the following:
+ [Environment integrity](environment-integrity.md)
+ [Releases](releases.md)
+ [Security](security.md)

To make it easier to identify the remnants of a legacy Git workflow in a modern configuration, let's compare [Gitflow](#gitflow-approach) to the modern, [trunk-based](#trunk-based-approach) approach.

## Gitflow approach
<a name="gitflow-approach"></a>

The following image shows a Gitflow workflow. The Gitflow approach uses multiple branches to track several different versions of the code at the same time. You schedule releases of updates to an application for some point in the future while developers still work on the current version of the code. Trunk-based repositories can use feature flags to accomplish this, but it's built in to Gitflow by default.

![A Gitflow workflow with feature, development, release, and hotfix branches](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-cicd-litmus/images/guide-img/de5d2132-0072-4b65-b7ac-e1e4c4852e08/images/1f3d6e7e-b0f7-442b-a932-b750d806b2c8.png)

One result of the Gitflow approach is that the application environments are usually out of sync. In a standard Gitflow implementation, development environments reflect the current state of the code while the preproduction and production environments remain frozen on the state of the code base from the most recent release.

This complicates things when a defect appears in the production environment because the code base that the developers work in cannot be merged into production without exposing unreleased features. The way Gitflow handles this situation is by using a hotfix. A hotfix branch is created from the release branch and then deployed straight into the upper environments. The hotfix branch is then merged into the development branch in order to keep the code current.

## Trunk-based approach
<a name="trunk-based-approach"></a>

The following image shows a trunk-based workflow. In a trunk-based workflow, developers build and test features locally in a feature branch and then merge those changes into the main branch. The main branch is then built to the development, preproduction, and production environments, sequentially. Unit and integration tests occur between each environment.

![A trunk-based workflow with feature branches and a main branch.](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-cicd-litmus/images/guide-img/de5d2132-0072-4b65-b7ac-e1e4c4852e08/images/024c2b91-8247-4d1a-b049-7d208461bef5.png)

Using this workflow, all environments are operating the same code base. There is no need for a hotfix branch for the upper environments because you can implement changes in the main branch without exposing unreleased features. The main branch is always assumed to be stable, free of defects, and ready to release. This helps you integrate it as a source for a CI/CD pipeline, which can automatically test and deploy your code base through all environments in your pipeline.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
