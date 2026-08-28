---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/example-of-session-revocation-code.html
---

# Example of session revocation code
<a name="example-of-session-revocation-code"></a>

```
//Import library
const awsSMD = require("./aws-secure-media-delivery");

//initialize Session class attributes, first argument points to DynamoDB //table which stores session to be revoked
awsSMD.Session.initialize('StackName-SessionToRevoke1234', {role:'arn:aws:iam::1234:role/stack_role', region: 'eu-west-2'});

async function blockSession(sessionId){
  //initiate instance of Session class with explicit sessionId provided
  let revokeSession = new awsSMD.Session(sessionId);
  let result = await revokeSession.revoke(86400);
  return result;
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Secure Media Delivery at the Edge on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
