---
source_url: https://docs.aws.amazon.com/ec2/latest/devguide/ec2-endpoints.html
---

# Amazon EC2 service endpoints

An endpoint is a URL that serves as an entry point for an AWS web service. Amazon EC2 supports the following endpoint types:
+ [IPv4 endpoints](#ipv4), which support IPv4 traffic only
+ [Dual-stack endpoints](#ipv6), which support both IPv4 and IPv6 traffic
+ [Zonal endpoints](#zonal-endpoints), which are dual-stack endpoints for a single Availability Zone and are in preview
+ [ FIPS endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#FIPS-endpoints), which use FIPS 140-validated cryptographic modules

When you make a request, you can specify the endpoint to use. If you do not specify an endpoint, the IPv4 endpoint is used by default. To use a different endpoint type, you must specify it in your request. For examples of how to do this, see [Specifying endpoints](#examples). For a table of available endpoints, see [Service endpoints by Region](#service-endpoints).

## IPv4 endpoints
<a name="ipv4"></a>

IPv4 endpoints support IPv4 traffic only. IPv4 endpoints are available for all Regions.

If you specify the general endpoint, `ec2.amazonaws.com`, we use the endpoint for `us-east-1`. To use a different Region, specify its associated endpoint. For example, if you specify `ec2.us-east-2.amazonaws.com` as the endpoint, we direct your request to the `us-east-2` endpoint.

IPv4 endpoint names use the following naming convention:
+ `{{service}}.{{region}}.amazonaws.com`

For example, the IPv4 endpoint name for the `eu-west-1` Region is `ec2.eu-west-1.amazonaws.com`.

## Dual-stack (IPv4 and IPv6) endpoints
<a name="ipv6"></a>

Dual-stack endpoints support both IPv4 and IPv6 traffic. When you make a request to a dual-stack endpoint, the endpoint URL resolves to an IPv6 or an IPv4 address, depending on the protocol used by your network and client.

Regional dual-stack endpoints include the AWS Region in the endpoint name. They use the following naming convention:
+ `ec2.{{region}}.api.aws`

For example, the dual-stack endpoint name for the `eu-west-1` Region is `ec2.eu-west-1.api.aws`.

Amazon EC2 also has dual-stack endpoints for individual Availability Zones, in preview. For more information, see [Zonal endpoints](#zonal-endpoints).

## Zonal endpoints
<a name="zonal-endpoints"></a>

**Note**
Zonal endpoints are in preview release for Amazon EC2 and are subject to change. For more information, see the Betas and Previews section of the [AWS Service Terms](https://aws.amazon.com/service-terms/) on the AWS website.

A zonal endpoint is an Amazon EC2 endpoint for a single Availability Zone. Amazon EC2 handles requests to a zonal endpoint in that Availability Zone, so issues in other Availability Zones are less likely to affect them. If your workload already runs separately in each Availability Zone, zonal endpoints let you isolate its Amazon EC2 API calls the same way.

Zonal endpoints are dual-stack and available for all Regions. Zonal endpoint names use the following naming conventions:
+ Dual-stack: `ec2-{{az-id}}.{{region}}.api.aws`
+ FIPS dual-stack, in the US and Canada Regions only: `ec2-fips-{{az-id}}.{{region}}.api.aws`

For example, the zonal endpoint name for `use1-az1` is `ec2-use1-az1.us-east-1.api.aws`.

The name uses the Availability Zone ID, such as `use1-az1`, not the Availability Zone name, such as `us-east-1a`. For more information about Availability Zone IDs, see [Availability Zone IDs for your AWS resources](https://docs.aws.amazon.com/ram/latest/userguide/working-with-az-ids.html).

To get the Availability Zone IDs for a Region, run the following [describe-availability-zones](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-availability-zones.html) command in the AWS Command Line Interface (AWS CLI).

```bash
PROMPT> aws ec2 describe-availability-zones \
    --region us-east-1 \
    --query "AvailabilityZones[].[ZoneName,ZoneId]" \
    --output table
```

### Resolving zonal endpoint request errors
<a name="zonal-endpoints-requests"></a>

Zonal endpoints accept requests for actions that work on resources in one Availability Zone, such as [RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html), [CreateVolume](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html), [AttachVolume](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AttachVolume.html), and [StopInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_StopInstances.html). The request must target resources in the endpoint's Availability Zone.

If a zonal endpoint can't process a request, it returns one of the following errors instead of forwarding the request to another Availability Zone:
+ `InvalidParameterValue`: The request targets a resource in a different Availability Zone. For example, you send a `RunInstances` request for a subnet in `use1-az2` to `ec2-use1-az1.us-east-1.api.aws`. Send the request to the zonal endpoint for the resource's Availability Zone.
+ `UnsupportedOperation`: Zonal endpoints don't support the action. This includes actions that don't work on resources in a single Availability Zone, such as `DescribeRegions`. Send the request to the regional endpoint.

Both are client errors, so retrying on the same zonal endpoint returns the same error. For more information, see [Error codes for the Amazon EC2 API](errors-overview.md).

### Zonal endpoint access control and auditing
<a name="zonal-endpoints-enforce"></a>

Use the `ec2:EndpointZone` condition key in IAM policies to control which endpoints principals can use. On requests to a zonal endpoint, the key contains the endpoint's Availability Zone ID. For more information about the condition keys for Amazon EC2, see [Actions, resources, and condition keys for Amazon EC2](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonec2.html) in the *Service Authorization Reference*.

The following policy denies `RunInstances` requests that don't use a zonal endpoint.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "RequireZonalEndpointForRunInstances",
            "Effect": "Deny",
            "Action": "ec2:RunInstances",
            "Resource": "*",
            "Condition": {
                "Null": {
                    "ec2:EndpointZone": "true"
                }
            }
        }
    ]
}
```

The following policy denies `RunInstances` and `CreateVolume` requests unless they use the `use1-az1` zonal endpoint.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "OnlyUse1Az1Endpoint",
            "Effect": "Deny",
            "Action": [
                "ec2:RunInstances",
                "ec2:CreateVolume"
            ],
            "Resource": "*",
            "Condition": {
                "StringNotEquals": {
                    "ec2:EndpointZone": "use1-az1"
                }
            }
        }
    ]
}
```

To audit which endpoint a request used, check the `clientProvidedHostHeader` field in the `tlsDetails` element of the CloudTrail event. For more information about the fields in a CloudTrail event, see [CloudTrail record contents](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.html) in the *AWS CloudTrail User Guide*.

## Service endpoints by Region
<a name="service-endpoints"></a>

The following are the service endpoints for Amazon EC2. For more information about Regions, see [Regions and Availability Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html) in the *Amazon EC2 User Guide*.

| Region Name | Region | Endpoint | Protocol |
| --- | --- | --- | --- |
| US East (Ohio) | us-east-2 |  ec2.us-east-2.amazonaws.com <br /> ec2-fips.us-east-2.amazonaws.com <br /> ec2.us-east-2.api.aws  | HTTP and HTTPS<br />HTTPS<br />HTTPS |
| US East (N. Virginia) | us-east-1 |  ec2.us-east-1.amazonaws.com <br /> ec2-fips.us-east-1.amazonaws.com <br /> ec2.us-east-1.api.aws  | HTTP and HTTPS<br />HTTPS<br />HTTPS |
| US West (N. California) | us-west-1 |  ec2.us-west-1.amazonaws.com <br /> ec2-fips.us-west-1.amazonaws.com <br /> ec2.us-west-1.api.aws  | HTTP and HTTPS<br />HTTPS<br />HTTPS |
| US West (Oregon) | us-west-2 |  ec2.us-west-2.amazonaws.com <br /> ec2-fips.us-west-2.amazonaws.com <br /> ec2.us-west-2.api.aws  | HTTP and HTTPS<br />HTTPS<br />HTTPS |
| Africa (Cape Town) | af-south-1 |  ec2.af-south-1.amazonaws.com <br /> ec2.af-south-1.api.aws  | HTTP and HTTPS<br />HTTPS |
| Asia Pacific (Hong Kong) | ap-east-1 |  ec2.ap-east-1.amazonaws.com <br /> ec2.ap-east-1.api.aws  | HTTP and HTTPS<br />HTTPS |
| Asia Pacific (Hyderabad) | ap-south-2 |  ec2.ap-south-2.amazonaws.com  | HTTPS |
| Asia Pacific (Jakarta) | ap-southeast-3 |  ec2.ap-southeast-3.amazonaws.com  | HTTPS |
| Asia Pacific (Malaysia) | ap-southeast-5 |  ec2.ap-southeast-5.amazonaws.com  | HTTPS |
| Asia Pacific (Melbourne) | ap-southeast-4 |  ec2.ap-southeast-4.amazonaws.com  | HTTPS |
| Asia Pacific (Mumbai) | ap-south-1 |  ec2.ap-south-1.amazonaws.com <br /> ec2.ap-south-1.api.aws  | HTTP and HTTPS<br />HTTPS |
| Asia Pacific (New Zealand) | ap-southeast-6 |  ec2.ap-southeast-6.amazonaws.com  | HTTPS |
| Asia Pacific (Osaka) | ap-northeast-3 |  ec2.ap-northeast-3.amazonaws.com  | HTTP and HTTPS |
| Asia Pacific (Seoul) | ap-northeast-2 |  ec2.ap-northeast-2.amazonaws.com <br /> ec2.ap-northeast-2.api.aws  | HTTP and HTTPS<br />HTTPS |
| Asia Pacific (Singapore) | ap-southeast-1 |  ec2.ap-southeast-1.amazonaws.com <br /> ec2.ap-southeast-1.api.aws  | HTTP and HTTPS<br />HTTPS |
| Asia Pacific (Sydney) | ap-southeast-2 |  ec2.ap-southeast-2.amazonaws.com <br /> ec2.ap-southeast-2.api.aws  | HTTP and HTTPS<br />HTTPS |
| Asia Pacific (Taipei) | ap-east-2 |  ec2.ap-east-2.amazonaws.com  | HTTPS |
| Asia Pacific (Thailand) | ap-southeast-7 |  ec2.ap-southeast-7.amazonaws.com  | HTTPS |
| Asia Pacific (Tokyo) | ap-northeast-1 |  ec2.ap-northeast-1.amazonaws.com <br /> ec2.ap-northeast-1.api.aws  | HTTP and HTTPS<br />HTTPS |
| Canada (Central) | ca-central-1 |  ec2.ca-central-1.amazonaws.com <br /> ec2-fips.ca-central-1.amazonaws.com <br /> ec2.ca-central-1.api.aws  | HTTP and HTTPS<br />HTTPS<br />HTTPS |
| Canada West (Calgary) | ca-west-1 |  ec2.ca-west-1.amazonaws.com <br /> ec2-fips.ca-west-1.amazonaws.com  | HTTPS<br />HTTPS |
| Europe (Frankfurt) | eu-central-1 |  ec2.eu-central-1.amazonaws.com <br /> ec2.eu-central-1.api.aws  | HTTP and HTTPS<br />HTTPS |
| Europe (Ireland) | eu-west-1 |  ec2.eu-west-1.amazonaws.com <br /> ec2.eu-west-1.api.aws  | HTTP and HTTPS<br />HTTPS |
| Europe (London) | eu-west-2 |  ec2.eu-west-2.amazonaws.com <br /> ec2.eu-west-2.api.aws  | HTTP and HTTPS<br />HTTPS |
| Europe (Milan) | eu-south-1 |  ec2.eu-south-1.amazonaws.com <br /> ec2.eu-south-1.api.aws  | HTTP and HTTPS<br />HTTPS |
| Europe (Paris) | eu-west-3 |  ec2.eu-west-3.amazonaws.com <br /> ec2.eu-west-3.api.aws  | HTTP and HTTPS<br />HTTPS |
| Europe (Spain) | eu-south-2 |  ec2.eu-south-2.amazonaws.com  | HTTPS |
| Europe (Stockholm) | eu-north-1 |  ec2.eu-north-1.amazonaws.com <br /> ec2.eu-north-1.api.aws  | HTTP and HTTPS<br />HTTPS |
| Europe (Zurich) | eu-central-2 |  ec2.eu-central-2.amazonaws.com  | HTTPS |
| Israel (Tel Aviv) | il-central-1 |  ec2.il-central-1.amazonaws.com  | HTTPS |
| Mexico (Central) | mx-central-1 |  ec2.mx-central-1.amazonaws.com  | HTTPS |
| Middle East (Bahrain) | me-south-1 |  ec2.me-south-1.amazonaws.com <br /> ec2.me-south-1.api.aws  | HTTP and HTTPS<br />HTTPS |
| Middle East (UAE) | me-central-1 |  ec2.me-central-1.amazonaws.com  | HTTPS |
| South America (São Paulo) | sa-east-1 |  ec2.sa-east-1.amazonaws.com <br /> ec2.sa-east-1.api.aws  | HTTP and HTTPS<br />HTTPS |
|  AWS GovCloud (US-East) | us-gov-east-1 |  ec2.us-gov-east-1.amazonaws.com <br /> ec2.us-gov-east-1.api.aws  | HTTPS<br />HTTPS |
|  AWS GovCloud (US-West) | us-gov-west-1 |  ec2.us-gov-west-1.amazonaws.com <br /> ec2.us-gov-west-1.api.aws  | HTTPS<br />HTTPS |

## Specifying endpoints
<a name="examples"></a>

This section provides some examples of how to specify an endpoint when making a request.

------
#### [ AWS CLI ]

The following examples show how to specify an endpoint for the `us-east-2` Region using the AWS CLI.
+ **Dual-stack**

  ```
  aws ec2 describe-regions --region us-east-2 --endpoint-url https://{{ec2.us-east-2.api.aws}}
  ```
+ **IPv4**

  ```
  aws ec2 describe-regions --region us-east-2 --endpoint-url https://{{ec2.us-east-2.amazonaws.com}}
  ```
+ **Zonal (preview)**

  The following example creates a volume in `use2-az1` by using the zonal endpoint for that Availability Zone. For more information about the requests that a zonal endpoint accepts, see [Resolving zonal endpoint request errors](#zonal-endpoints-requests).

  ```
  aws ec2 create-volume --region us-east-2 \
      --availability-zone-id use2-az1 \
      --size 8 \
      --endpoint-url https://{{ec2-use2-az1.us-east-2.api.aws}}
  ```

------
#### [ AWS SDK for Java 2.x ]

The following examples show how to specify an endpoint for the `us-east-2` Region using the AWS SDK for Java 2.x.
+ **Dual-stack**

  ```
  Ec2Client client = Ec2Client.builder()
      .region(Region.US_EAST_2)
      .endpointOverride(URI.create("https://{{ec2.us-east-2.api.aws}}"))
      .build();
  ```
+ **IPv4**

  ```
  Ec2Client client = Ec2Client.builder()
      .region(Region.US_EAST_2)
      .endpointOverride(URI.create("https://{{ec2.us-east-2.amazonaws.com}}"))
      .build();
  ```
+ **Zonal (preview)**

  The following example creates a client that sends requests to the zonal endpoint for `use2-az1`.

  ```java
  import java.net.URI;

  import software.amazon.awssdk.regions.Region;
  import software.amazon.awssdk.services.ec2.Ec2Client;

  public class ZonalEndpointExample {
      public static void main(String[] args) {
          try (Ec2Client client = Ec2Client.builder()
                  .region(Region.US_EAST_2)
                  .endpointOverride(URI.create("https://{{ec2-use2-az1.us-east-2.api.aws}}"))
                  .build()) {
              // Send requests for resources in use2-az1.
          }
      }
  }
  ```

------
#### [ AWS SDK for Java 1.x ]

The following examples show how to specify an endpoint for the `eu-west-1` Region using the AWS SDK for Java 1.x.
+ **Dual-stack**

  ```
  AmazonEC2 s3 = AmazonEC2ClientBuilder.standard()
       .withEndpointConfiguration(new EndpointConfiguration(
            "https://{{ec2.eu-west-1.api.aws}}",
            "eu-west-1"))
       .build();
  ```
+ **IPv4**

  ```
  AmazonEC2 s3 = AmazonEC2ClientBuilder.standard()
       .withEndpointConfiguration(new EndpointConfiguration(
            "https://{{ec2.eu-west-1.amazonaws.com}}",
            "eu-west-1"))
       .build();
  ```

------
#### [ AWS SDK for Go ]

The following examples show how to specify an endpoint for the `us-east-1` Region using the AWS SDK for Go.
+ **Dual-stack**

  ```
  sess := session.Must(session.NewSession())
  svc := ec2.New(sess, &aws.Config{
      Region: aws.String(endpoints.UsEast1RegionID),
      Endpoint: aws.String("https://{{ec2.us-east-1.api.aws}}")
  })
  ```
+ **IPv4**

  ```
  sess := session.Must(session.NewSession())
  svc := ec2.New(sess, &aws.Config{
      Region: aws.String(endpoints.UsEast1RegionID),
      Endpoint: aws.String("https://{{ec2.us-east-1.amazonaws.com}}")
  })
  ```

------
