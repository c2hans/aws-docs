---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/unexpected-hangups.html
---

# Debugging unexpected hangups in the Amazon Chime SDK PTSN audio service
<a name="unexpected-hangups"></a>

Complete the following troubleshooting actions if you experience unexpected hangups or error messages with AWS Lambda functions for the PSTN audio service:
+ Verify that your AWS Lambda policy grants the `lambda:InvokeFunction` permission to the [voiceconnector.chime.amazonaws.com](http://voiceconnector.chime.amazonaws.com/) service principal.
+ Check the logs for your AWS Lambda function to ensure that it's being successfully invoked.
+ If the logs show incoming events and returned actions, verify that you don't return a hangup action in when the AWS Lambda function is invoked.
+ Check the CloudWatch logs for your SIP media application. The following table lists some of the messages you may encounter.

<table>
<thead>
  <tr><th>Message</th><th>Resolution</th></tr>
</thead>
<tbody>
  <tr><td>AWS Lambda client operation timed out.</td><td>The function took longer than 20 seconds to complete. Shorten the response time to less than 20 seconds.</td></tr>
  <tr><td>Access denied while invoking the AWS Lambda function.</td><td>The AWS Lambda function doesn't provide a policy that allows the service to access the Amazon Chime SDK Voice Connector service principal. Provide the <code>voiceconnector.chime.amazonaws.com</code> service principal with the <code>lambda:InvokeFunction</code> permission in your AWS Lambda policies.</td></tr>
  <tr><td>The AWS Lambda function was throttled.</td><td>The Audio Service couldn't call your AWS Lambda function because the function was throttled. For more information, see <a href="https://aws.amazon.com/premiumsupport/knowledge-center/lambda-troubleshoot-throttling/"> https://aws.amazon.com/premiumsupport/knowledge-center/lambda-troubleshoot-throttling/</a>. </td></tr>
  <tr><td>Error while reading actions list.</td><td>The PSTN audio service failed to parse the actions returned by your AWS Lambda function. Check the logs for <code>ACTION_FAILED</code> events, and consult the documentation for the failed action to ensure that you coded it properly.</td></tr>
  <tr><td>The schema version in the invocation request does not match the schema version in the response.</td><td>Check your logs and ensure that your request and response use the same schema version.</td></tr>
  <tr><td>Unsupported action <i>name</i> specified</td><td>The AWS Lambda function returned an action that the PSTN audio service didn't recognize. Ensure the action is spelled correctly, and see the documentation for the action.</td></tr>
  <tr><td>Actions list is empty.</td><td>The response to a <code>NEW_INCOMING_CALL</code> event didn't return any actions. Return an action in response to that event.</td></tr>
  <tr><td>Too many actions specified in a response.</td><td>You returned more than 10 actions in response to an AWS Lambda invocation. Return 10 or fewer actions.</td></tr>
  <tr><td>Response is blank or empty</td><td>You returned a null or an empty string. Make sure the response object includes at least the <code>SchemaVersion</code> field.</td></tr>
</tbody>
</table>
