---
source_url: https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/establish-preventive-controls-across-your-environment.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Establish preventive controls across your environment
<a name="establish-preventive-controls-across-your-environment"></a>

Only granting permissions does not guarantee that our environment is fully secured. To ensure that only the services that are intended to be used by the assigned roles, you need to limit what actions can be performed in your overall environment. For example, to limit the modification of the logs that are being stored in your log storage.

To prevent anyone from deleting or modifying these logs by mistake, you need to enable preventive controls to restrict the deletion on the logs in your log storage. On AWS this can be accomplished by applying [service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) to your accounts. These policies allow you to limit certain actions within a specific account, but you can also use them to prevent access to services completely, or limit the actions in your environment in specific regions that are not approved for use in your environment.
