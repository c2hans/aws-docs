---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-cicd-litmus/faq.html
---

# FAQ
<a name="faq"></a>

## What are some key indicators that my deployment process is not fully CI/CD?
<a name="faq-key-indicators"></a>

The most common indicator is when there are multiple repository branches that represent separate environments in a pipeline. Repositories in a fully CI/CD process use a trunk-based workflow, in which one branch acts as the single source of truth for that repository's deployments. For more information, see [Trunk-based approach](fully-cicd-process-differences.md#trunk-based-approach). Other indicators include manual deployment steps other than simple go or no-go decisions, the use of hotfixes, and scheduled releases.

## What if I want to use a fully CI/CD process but still want to schedule releases of certain features for specific points in time?
<a name="faq-scheduled-releases"></a>

This is usually done with feature flags. In this process, deployments are still made continuously, but certain features are hidden by using conditional closures in the code until it is time to release them.

## What if some steps in my deployment process can't be automated?
<a name="faq-automated-steps"></a>

One of the goals of a fully CI/CD pipeline is to minimize the need for manual processes, but there are certainly potential use cases where manual processes may be necessary. In fact, read-only processes, such as consulting application logs, can often be done in production environments with minimal risk. However, it is strongly recommended that you treat manual write actions in production as an absolute last resort.

## What if my technical staff is more comfortable with legacy workflows than with a fully CI/CD process?
<a name="faq-resistance-to-change"></a>

It's common for technical staff to be resistant to major changes, especially when something that used to be a best practice is replaced by something newer. Technology moves fast, and improvements are constantly being discovered. Although a certain degree of skepticism is a good quality for a technical staff to have, it's just as important for them to be open to change. Don't move too fast with skeptical staff because they need to manage changes to the system before they are implemented. The key is to prevent skeptics from remaining static forever.

## What if my environments are in multiple accounts? Can I still use a fully CI/CD process?
<a name="faq-multiple-accounts"></a>

Yes, in fact, it's recommended to use a separate account for each environment. For more information about a pipeline that activates stages in different accounts, see [Create a pipeline in CodePipeline that uses resources from another AWS account](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-create-cross-account.html).
