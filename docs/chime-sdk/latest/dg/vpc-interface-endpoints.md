---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/vpc-interface-endpoints.html
---

# AWS PrivateLink for Amazon Chime SDK
<a name="vpc-interface-endpoints"></a>

With AWS PrivateLink, you can create interface virtual private cloud (VPC) endpoints to access Amazon Chime SDK Voice, Amazon Chime SDK Meetings, Amazon Chime SDK Messaging, Amazon Chime SDK Identity, and Amazon Chime SDK Media Pipelines APIs directly from your VPC. When you use an interface endpoint, traffic between your VPC and these services stays within the AWS network and doesn't traverse the public internet.

Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink/), which enables private connectivity to Amazon Chime SDK APIs using private IP addresses. You don't need an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. For more information about AWS PrivateLink, see the [AWS PrivateLink Guide](https://docs.aws.amazon.com/vpc/latest/privatelink/).

## Considerations
<a name="vpc-endpoint-considerations"></a>
+ Interface endpoints route API requests only. The following types of traffic do not support PrivateLink:
  + PSTN audio and media streams (Amazon Chime SDK Voice)
  + SIP signaling and media for Voice Connectors (Amazon Chime SDK Voice)
  + Meeting media, including audio and video (Amazon Chime SDK Meetings)
  + WebSocket connections for real-time messaging (Amazon Chime SDK Messaging)
  + Meeting media capture and live streaming (Amazon Chime SDK Media Pipelines)
+ SIP traffic to and from Voice Connectors uses direct IP connectivity and does not traverse interface endpoints.
+ When you use an interface endpoint, all API calls from your VPC go through the endpoint. This applies to calls made with an AWS SDK or the AWS CLI, such as calls to create voice connectors, start meetings, send messages, or manage media pipelines.
+ Interface endpoints support both IPv4 and IPv6 (dualstack) traffic.
+ Interface endpoints support VPC endpoint policies. You can use endpoint policies to control which principals can use the endpoint and which API actions they can perform.
+ FIPS endpoints through PrivateLink are available in the following Regions:
[See the AWS documentation website for more details](http://docs.aws.amazon.com/chime-sdk/latest/dg/vpc-interface-endpoints.html)
+ In AWS GovCloud (US) Regions, interface endpoints use FIPS by default, and IAM policies use the `aws-us-gov` partition.

## Creating an interface endpoint
<a name="vpc-endpoint-create"></a>

You can create an interface endpoint for Amazon Chime SDK services using the Amazon VPC console or the AWS Command Line Interface. For more information about creating endpoints, see [Create a VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *AWS PrivateLink Guide*.

Create an interface endpoint using one of the following service names:

```
com.amazonaws.{{region}}.chime-sdk-voice
com.amazonaws.{{region}}.meetings-chime
com.amazonaws.{{region}}.messaging-chime
com.amazonaws.{{region}}.identity-chime
com.amazonaws.{{region}}.media-pipelines-chime
```

The following example uses the AWS CLI to create an interface endpoint for Amazon Chime SDK Meetings. To create an endpoint for a different service, replace the service name accordingly (for example, `com.amazonaws.us-east-1.chime-sdk-voice` for Voice).

```
aws ec2 create-vpc-endpoint \
    --vpc-id {{vpc-1a2b3c4d}} \
    --vpc-endpoint-type Interface \
    --service-name com.amazonaws.{{us-east-1}}.meetings-chime \
    --subnet-ids {{subnet-abababab}} \
    --security-group-ids {{sg-1a2b3c4d}}
```

## Private DNS
<a name="vpc-endpoint-private-dns"></a>

When you create an interface endpoint with private DNS enabled, you can make API requests to Amazon Chime SDK services using the following endpoint DNS names:

Amazon Chime SDK Voice
+ `voice-chime.{{region}}.amazonaws.com`
+ `voice-chime.{{region}}.api.aws`

Amazon Chime SDK Meetings
+ `meetings-chime.{{region}}.amazonaws.com`
+ `meetings-chime.{{region}}.api.aws`

Amazon Chime SDK Messaging
+ `messaging-chime.{{region}}.amazonaws.com`
+ `messaging-chime.{{region}}.api.aws`

Amazon Chime SDK Identity
+ `identity-chime.{{region}}.amazonaws.com`
+ `identity-chime.{{region}}.api.aws`

Amazon Chime SDK Media Pipelines
+ `media-pipelines-chime.{{region}}.amazonaws.com`
+ `media-pipelines-chime.{{region}}.api.aws`

With private DNS enabled, you don't need to make any changes to your application code or SDK configuration. Requests to the standard Amazon Chime SDK endpoints automatically route through the interface endpoint.

For more information about private DNS, see [Private DNS](https://docs.aws.amazon.com/vpc/latest/privatelink/manage-dns-names.html) in the *AWS PrivateLink Guide*.

### FIPS endpoints
<a name="vpc-endpoint-fips-dns"></a>

Amazon Chime SDK Voice FIPS endpoints are available in US East (N. Virginia), US West (Oregon), and Canada (Central):
+ `voice-chime-fips.{{region}}.amazonaws.com`
+ `voice-chime-fips.{{region}}.api.aws`

Amazon Chime SDK Meetings FIPS endpoints are available in US East (N. Virginia), US West (Oregon), Canada (Central), AWS GovCloud (US-East), and AWS GovCloud (US-West):
+ `meetings-chime-fips.{{region}}.amazonaws.com`
+ `meetings-chime-fips.{{region}}.api.aws`

Amazon Chime SDK Messaging FIPS endpoints are available in US East (N. Virginia):
+ `messaging-chime-fips.{{region}}.amazonaws.com`
+ `messaging-chime-fips.{{region}}.api.aws`

Amazon Chime SDK Identity FIPS endpoints are available in US East (N. Virginia):
+ `identity-chime-fips.{{region}}.amazonaws.com`
+ `identity-chime-fips.{{region}}.api.aws`

Amazon Chime SDK Media Pipelines FIPS endpoints are available in US East (N. Virginia), US West (Oregon), and Canada (Central):
+ `media-pipelines-chime-fips.{{region}}.amazonaws.com`
+ `media-pipelines-chime-fips.{{region}}.api.aws`

## Creating a VPC endpoint policy
<a name="vpc-endpoint-policy"></a>

You can attach a VPC endpoint policy to control access to Amazon Chime SDK APIs through the endpoint. The policy specifies the following:
+ The principals that can perform actions
+ The actions that can be performed
+ The resources on which actions can be performed

For more information about endpoint policies, see [VPC endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the *AWS PrivateLink Guide*.

**Example Restrict endpoint to specific actions**
The following endpoint policy allows all principals to call `GetVoiceConnector` and `ListVoiceConnectors` (Voice), `CreateMeeting` and `GetMeeting` (Meetings), and `CreateMediaCapturePipeline` and `ListMediaPipelines` (Media Pipelines) through the endpoint, but denies all other actions.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "chime:GetVoiceConnector",
                "chime:ListVoiceConnectors",
                "chime:CreateMeeting",
                "chime:GetMeeting",
                "chime:CreateMediaCapturePipeline",
                "chime:ListMediaPipelines"
            ],
            "Resource": "*"
        }
    ]
}
```

**Example Restrict access to a specific VPC endpoint**
The following IAM policy denies access to Amazon Chime SDK APIs unless the request originates from a specific VPC endpoint. Use the `aws:sourceVpce` condition key to restrict access.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Deny",
            "Action": "chime:*",
            "Resource": "*",
            "Condition": {
                "StringNotEquals": {
                    "aws:sourceVpce": "{{vpce-1a2b3c4d}}"
                }
            }
        }
    ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
