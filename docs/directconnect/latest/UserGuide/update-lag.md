---
source_url: https://docs.aws.amazon.com/directconnect/latest/UserGuide/update-lag.html
---

# Update a LAG at a Direct Connect endpoint
<a name="update-lag"></a>

You can update the following link aggregation group (LAG) attributes using either the Direct Connect console or using the command line or API:
+ The name of the LAG.
+ The value for the minimum number of connections that must be operational for the LAG itself to be operational.
+ The LAG's MACsec encryption mode.

  MACsec is only available on dedicated connections.

  AWS assigns this value to each connection that is part of the LAG.

  The valid values are:
  + `should_encrypt`
  + `must_encrypt`

    When you set the encryption mode to this value, the connections go down when the encryption is down.
  + `no_encrypt`
+ The tags.

**Note**
If you adjust the threshold value for the minimum number of operational connections, ensure that the new value does not cause the LAG to fall below the threshold and become non-operational.

**To update a LAG**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **LAGs**.

1. Select the LAG, and then choose **Edit**.

1. Modify the LAG

   [Change the name] For **LAG Name**, enter a new LAG name.

   [Adjust the minimum number of connections] For **Minimum Links**, enter minimum number of operational connections.

   [Add a tag] Choose **Add tag** and do the following:
   + For **Key**, enter the key name.
   + For **Value**, enter the key value.

   [Remove a tag] Next to the tag, choose **Remove tag**.

1. Choose **Edit LAG**.

**To update a LAG using the command line or API**
+ [update-lag](https://docs.aws.amazon.com/cli/latest/reference/directconnect/update-lag.html) (AWS CLI)
+ [UpdateLag](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_UpdateLag.html) (Direct Connect API)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Direct Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
