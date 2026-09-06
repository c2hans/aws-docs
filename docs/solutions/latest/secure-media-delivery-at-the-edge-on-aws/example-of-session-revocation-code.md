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
