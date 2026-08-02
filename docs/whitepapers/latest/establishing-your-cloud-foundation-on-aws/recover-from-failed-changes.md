---
source_url: https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/recover-from-failed-changes.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Recover from failed changes
<a name="recover-from-failed-changes"></a>

Changes should not be approved without considering the consequences of a failure or degraded performance outcome. There should be a back-out or rollback plan which will restore the resource to its initial baseline configuration prior to the executed change. The cloud enables *rollback* plans to be fully automated using repeatable processes. Not all changes are reversible. However, the process to recover from failed changes should be documented and the risk accepted when approving the change. If failed changes have a much lower impact due to the speed and consistency of roll back, activating roll-backs should be considered to be part of the normal process. This is particularly true if it is possible to quickly remediate the issue and push it through the same automated pipelines to quickly deliver the original intended business value of the change.
