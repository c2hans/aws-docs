---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/example-of-token-generation-code.html
---

# Example of token generation code
<a name="example-of-token-generation-code"></a>

 Below code snippet serves as an example to show the sequence of steps that needs to be reflected in the code to produce a token at the level of playback API endpoint. It does not include the logic required to obtain the information about the video assets or how to compose viewer attributes and token policy objects, which would be specific to your use case and integration with content management system. In the API module, Lambda functions are deployed and can be considered as a more complete reference example of how to implement complementary logic and combine it with the solution’s library.

```
//Import library
const awsSMD = require("./aws-secure-media-delivery");

//create secret instance, parameters specify stack name, secret caching

//ttl, 'native' informs to use AWS SecretsManager client for key retrieval
let secret = new awsSMD.Secret('StackName',10,'native');

//initiate AWS Secrets Manager client associated with secret instance
//role refers to the solution created role, region specifies in which region
//signing keys are stored in Secrets Manager
secret.initSMClient({role:'arn:aws:iam::1234:role/stack_role', region: 'eu-west-2'})
//initiate instance of Token class and associate it with secret object
let token = new awsSMD.Token(secret);

async function vendToken(viewer_attributes, playback_url, token_policy){

//generate the token
let outputToken = await token.generate(viewer_attributes, playback_url, token_policy);
return outputToken;
}
```
