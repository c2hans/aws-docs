---
source_url: https://docs.aws.amazon.com/directconnect/latest/UserGuide/associate-key-lag.html
---

# Associate a MACsec CKN/CAK with a Direct Connect endpoint LAG
<a name="associate-key-lag"></a>

After you create the LAG that supports MACsec, you can associate a CKN/CAK with the connection using either the Direct Connect console or using the command line or API.

**Note**
You cannot modify a MACsec secret key after you associate it with a LAG. If you need to modify the key, disassociate the key from the connection, and then associate a new key with the connection. For information about removing an association, see [Remove the association between a MACsec secret key and a Direct Connect endpoint LAG](disassociate-key-lag.md).

**To associate a MACsec key with a LAG**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **LAGs**.

1. Select the LAG and choose **View details**.

1. Choose **Associate key**.

1. Enter the MACsec key.

   [Use the CAK/CKN pair] Choose **Key Pair**, and then do the following:
   + For **Connectivity Association Key (CAK)**, enter the CAK.
   + For **Connectivity Association Key Name (CKN)**, enter the CKN.

   [Use the secret] Choose **Existing Secret Manager secret**, and then for **Secret**, select the MACsec secret key.

1. Choose **Associate key**.

**To associate a MACsec key with a LAG using the command line or API**
+ [associate-mac-sec-key](https://docs.aws.amazon.com/cli/latest/reference/directconnect/associate-mac-sec-key.html) (AWS CLI)
+ [AssociateMacSecKey](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AssociateMacSecKey.html) (Direct Connect API)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Direct Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
