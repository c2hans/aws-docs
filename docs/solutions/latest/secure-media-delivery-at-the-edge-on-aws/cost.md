---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/cost.html
---

# Cost
<a name="cost"></a>

 You are responsible for the cost of the AWS services used while running this solution. The total cost for running this solution depends on the selected modules used in the solution and input parameters.

 We recommend creating a [budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html) through [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to help manage costs. Prices are subject to change. For full details, see the pricing webpage for each [AWS service used in this solution](architecture-details.md#aws-services).

**Note**
 Below cost estimates relate only to the elements created during the deployment of the solution. The charges associated with running the video workload on CloudFront, which must be created independently from this solution, are not included in the cost breakdown.
 Example cost calculations listed below demonstrate incremental costs incurred from newly created components in your account as an output of the solution.
 The total charges will also include the video delivery pipeline that consist of costs of running media content origin (for example, Amazon S3, AWS Elemental MediaPackage, among others) and delivery to the viewers through Amazon CloudFront. These costs are not specified below as this solution is designed to complement existing video streaming workloads implemented on Amazon CloudFront.

 **Assumptions**
+  The following examples provide a cost estimate for video streaming workload with 10 live streaming events per month, 60 mins in duration each, and driving 10,000 concurrent viewers. For each viewer, a playback token is generated once, just before the playout starts. It is assumed that during each event, 10 playback sessions are revoked manually, while 20 of them are detected and blocked as a result of automatic session revocation mechanism.
+  Signing key is rotated automatically each day.
+  To calculate the number of CloudFront Function invocations (example):

  1. Number of viewing sessions 10,000 viewers \* 10 events = 100,000 sessions

  1. Average viewing duration per session (seconds) 60 minutes \* 60 = 3600 seconds

  1. Segment length (seconds) 2 seconds and manifest request after 3 consecutive segment requests (3600/2 \+ 3600/(2\*3) \*100000 = 240M invocations

## Base module
<a name="base-module-1"></a>

*Cost to validate request tokens and key rotation *

<table>
<thead>
  <tr><th>AWS service </th><th> <b>Dimension/month</b> </th><th> <b>Cost [USD]</b> </th></tr>
</thead>
<tbody>
  <tr><td> CloudFront Functions </td><td> 240 million invocations </td><td> $24.00 </td></tr>
  <tr><td> Secrets Manager </td><td> 3 secrets API call for 1 in 10 token generation operations Storage per secret per month </td><td> $1.25 $0.40 * number of keys </td></tr>
  <tr><td> Step Functions </td><td> Number of transitions during key rotation workflow One rotation per day ~ 30/mo </td><td> &lt; $0.01 </td></tr>
  <tr><td> Lambda </td><td> Lambda related costs during key rotation process One rotation per day ~ 30/mo </td><td> &lt; $0.01 </td></tr>
  <tr><td colspan="2"> <b>Total monthly cost:</b> </td><td> <b>~$25.65 / month</b></td></tr>
</tbody>
</table>

**Note**
 This solution uses [secrets key caching implemented in token generation method for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets.html) to reduce API calls and cost

## Session revocation
<a name="session-revocation"></a>

 **(Part of base module but it’s optional to use it)**

*Cost to block compromised playback sessions*

<table>
<thead>
  <tr><th>AWS service </th><th> <b>Dimension/month</b> </th><th> <b>Cost [USD]</b> </th></tr>
</thead>
<tbody>
  <tr><td> AWS WAF </td><td> Web ACL + Rule Group + Rules (*it is assumed no WebACL was not used before for video delivery and AWS WAF is associated with CloudFront solely for session revocation purpose) </td><td> $6.14 </td></tr>
  <tr><td> AWS WAF </td><td> Requests – 240 million (*it is assumed no web ACL was not used before for video delivery and AWS WAF is associated with CloudFront solely for session revocation purpose) </td><td> $144.00 </td></tr>
  <tr><td colspan="2"> <b>Total monthly cost:</b> </td><td> <b>~$150.14 / month</b> </td></tr>
</tbody>
</table>

## API Module
<a name="api-module-1"></a>

 **(Part of core module but it’s optional to use it)**

*Cost to generate 100,000 of playback tokens per month *

<table>
<thead>
  <tr><th>AWS service </th><th> <b>Dimension/month</b> </th><th> <b>Cost [USD]</b> </th></tr>
</thead>
<tbody>
  <tr><td> API Gateway </td><td> 100,000 API calls </td><td> $0.10 </td></tr>
  <tr><td> DynamoDB </td><td> 50,000 Read Request Units Assume 1 request = .5 RRU </td><td> $0.01 </td></tr>
  <tr><td> CloudFront (fronting API Gateway) (Data Transfer + Request charges) </td><td> 100,000 HTTP requests with ~1kB response </td><td> $0.11 </td></tr>
  <tr><td> Lambda@Edge </td><td> 100,000 function invocations </td><td> $0.60 </td></tr>
  <tr><td> Lambda </td><td> 100,000 function invocations </td><td> $0.20 </td></tr>
  <tr><td colspan="2"> <b>Total monthly cost:</b> </td><td> <b>~$0.48 / month</b> </td></tr>
</tbody>
</table>

**Note**
 Cost for API calls to Secrets Manager already included in Base module

## Auto session-revocation
<a name="auto-session-revocation"></a>

 **(In addition to session revocation costs)**

*Cost to run auto revocation pipeline*

<table>
<thead>
  <tr><th>AWS service </th><th> <b>Dimension/month</b> </th><th> <b>Cost [USD]</b> </th></tr>
</thead>
<tbody>
  <tr><td> Step Functions </td><td> Number of transitions during session scanning and updating workflow </td><td> $0.14 </td></tr>
  <tr><td> Athena </td><td> CloudFront Access Logs Data Scanned* - 1545GB <i>* (single 1hr playback session produces ~270KB log data)</i> </td><td> $7.54 </td></tr>
  <tr><td> AWS WAF </td><td> Additional rules inserted into Rule Group from Session Revocation </td><td> $0.27 </td></tr>
  <tr><td colspan="2"> <b>Total monthly cost:</b> </td><td> <b>$7.95 / month</b> </td></tr>
</tbody>
</table>

## Metrics monitoring
<a name="metrics-monitoring"></a>

 *Cost of running the solution’s dashboard*

<table>
<thead>
  <tr><th>AWS service </th><th> <b>Dimension/month</b> </th><th> <b>Cost [USD]</b> </th></tr>
</thead>
<tbody>
  <tr><td> CloudWatch - Dashboard </td><td> Fixed cost for CloudWatch Dashboard </td><td> $5.00 </td></tr>
  <tr><td> CloudWatch Logs Insights – Data Scanned </td><td> Token verification results widget built on CloudWatch Logs insights – 72GB data scanned </td><td> $0.36 </td></tr>
  <tr><td colspan="2"> <b>Total monthly cost:</b> </td><td> <b>~$5.36 / month</b> </td></tr>
</tbody>
</table>

 If you choose to deploy the demo website (which we recommend deactivating after you launch the solution in a production environment), the solution automatically deploys Amazon S3 bucket for storing the static website assets in your account, and use the same CloudFront distribution created in front of API Gateway endpoint. You are responsible for the incurred variable charges from these services.
