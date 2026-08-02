---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/solution-workflow.html
---

# Solution workflow
<a name="solution-workflow"></a>

 This solution provides code constructs (as a NodeJS library) that makes it simpler to generate a token upon verifying the viewer’s permissions when playback URL is requested. Integrating token generation into authorization flow in your application is a key element in the effectiveness of the solution.

**Important**
 The solution-created demo website module creates a simple website, which is meant to provide a proof-of-concept and troubleshooting phases for testing the solution. However, you should eventually replace it with an end-user application and viewer authorization components.

 One of the primary objectives of this solution is to provide a uniformly supported mechanism across a variety of client types. The main consideration in that regard is to use a universally supported method to carry the tokens. In this solution, the generated token is embedded in the playback URL to ensure a video player does not drop the token, which would be possible if other methods for carrying the token were used.

 **Acquiring playback URL with the token**

1.  When the viewer wishes to play a specific video content, client-side application makes an API call to `Playback` API that is expected to respond with the playback URL including the token.

1.  When a request reaches `Playback` API, the request is validated to ensure if the viewer has permissions to watch requested video content (as outlined above, this step needs to be added by users of the solution).

1.  Once it is verified that the client is authorized to watch the requested content, an internal call is initiated to construct a playback URL containing the token for that specific viewer. In the solution’s implementation, this call is served by API Gateway through Lambda function associated with the `/tokengenerate` path.

1.  The service responsible for token generation retrieves information about the requested video asset, and token parameters, to issue a playback URL including the token for requesting viewer. As specified by token policy, token includes certain attributes that are associated to the viewer (user-agent, source IP, etc.) and restrict access only to the requested video asset. If specified in the token policy, provided library will also generate a random playback session ID that will be signed.

 The Playback API serves back the playback URL for requested asset, including the token with the session ID.

 **Client requesting video assets and token validation**

1.  After the client-side application acquires the playback URL with the token, it is passed on to the video player, which initiates sequential requests for video manifest and video segments.

1.  As the request reaches CloudFront distribution, it is first run through attached AWS WAF web ACL (if included in the CloudFront distribution configuration), which includes the rule group with rules to match the sessions that were previously submitted to be blocked.

1.  If the session ID corresponding to the request was not blocked by AWS WAF, Amazon CloudFront Function inspects the token retrieved from the URL path. If all signatures match, the token is unexpired, and the token covers requested video asset, the request is allowed and the token is removed from the URL path. After that, the request continues on the normal Amazon CloudFront processing path.

 **Revoking compromised playback session**

 *Manual path*

1.  After a solution operator discovers a compromised playback session that should be blocked, an API call can be made to revoke such a session, and start blocking any subsequent requests linked to that session.

1.  Amazon API Gateway verifies if the request is coming from an authorized user, and initiates session revocation methods exposed through provided solution library.

1.  Session revocation method pushes the session ID to the target DynamoDB table which in turn invokes a Lambda function associated with a DynamoDB data stream.

1.  The invoked Lambda function goes through the list of the sessions in the DynamoDB table, prioritizes them, and reduces the list to the size that can be accommodated within the AWS WAF rule group. Eventually, Lambda function updates WAF rule group with the updated list of sessions that must be revoked.

 *Automatic session revocation path*

1.  As the traffic flows through the CloudFront distribution, access logs are continuously emitted to an Amazon S3 bucket (logs can be further partitioned as per [Analyze your Amazon CloudFront access logs at scale](https://aws.amazon.com/blogs/big-data/analyze-your-amazon-cloudfront-access-logs-at-scale)).

1.  At a periodic frequency set by the user, an AWS EventBridge rule invokes a Step Functions workflow. The task of that workflow is to analyze the logs in the S3 bucket holding access logs to identify the sessions with unusual traffic composition that suggest the sessions have been compromised (meaning more than one viewer uses the same playback session ID to retrieve the stream).

1.  A Lambda function is invoked through the Step Functions workflow to generate a SQL query that incorporates input parameters set by the solution’s client and limits the time window for the logs subject to analysis.

1.  A SQL query is submitted to Amazon Athena, which performs the job and outputs a list of session IDs that exceed suspicious threshold.

1.  Another Lambda function in the Step Functions workflow checks if the job is complete, and pulls the output result for further processing. Athena sourced session IDs are populated into the DynamoDB table that holds the list of sessions that must be revoked.

1.  Changes to the DynamoDB table initiate DynamoDB streams that invokes the associated Lambda function as a result.

1.  Invoked Lambda function goes through the list of the sessions in DynamoDB table, prioritize them according to the predefined criteria, and reduce the list to the size that can be accommodated within AWS WAF rule group. Eventually, the Lambda function updates WAF rule group with the updated list of sessions that must be revoked.

 **Key rotation**

1.  An EventBridge rule is initiated periodically at a time set by the solution’s client when the solution is deployed.

1.  After initial deployment of the solution and every time EventBridge rule runs, a key rotation Step Functions workflow is started.

1.  A Lambda function called by Step Functions workflow generates a random signing key which is used to sign the token through library methods, and validates the token by CloudFront Function logic.

1.  Before the newly generated key replaces the existing key stored as the primary secret in AWS Secrets Manager**,** that new key is first updated in CloudFront Function code, and the new code is published.

1.  Step Functions workflows check whether that change was successfully updated and propagated through CloudFront Functions. Once confirmed, workflows progress to the next step.

1.  The newly created key is promoted as the primary key and replaces the key value of primary secret in Secrets Manager.

1.  At this point, when the library method generating token retrieves keys from Secrets Manager it uses a new primary key, which is also available in CloudFront Functions.
