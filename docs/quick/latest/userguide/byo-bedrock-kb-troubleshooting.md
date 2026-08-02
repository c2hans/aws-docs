---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/byo-bedrock-kb-troubleshooting.html
---

# Troubleshooting
<a name="byo-bedrock-kb-troubleshooting"></a>

## Access denied when querying the knowledge base
<a name="byo-bedrock-kb-access-denied"></a>

**Symptoms**
+ Users receive access denied errors when querying the knowledge base.

**Resolution**
+ For cross-account setups, verify that the resource policy on the knowledge base grants `bedrock:Retrieve` and `bedrock:GetDocumentContent` to the Amazon Quick service role.
+ Verify the knowledge base ARN is correct in the Amazon Quick admin configuration.
+ Confirm the knowledge base and Amazon Quick instance are in the same Region.

## No results returned from knowledge base
<a name="byo-bedrock-kb-no-results"></a>

**Symptoms**
+ Queries return no results even though the knowledge base has indexed data.

**Resolution**
+ Check AWS CloudTrail logs to verify that retrieval requests are reaching the knowledge base and inspect any error responses.
+ Work with the knowledge base owner to verify the knowledge base has been synced and contains indexed documents.
+ If using ACL-enabled connectors, confirm the user's email matches an authorized identity in the data source.
