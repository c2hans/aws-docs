---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeReservedInstanceOfferings.html
---

# DescribeReservedInstanceOfferings
<a name="API_DescribeReservedInstanceOfferings"></a>

Describes the available Amazon OpenSearch Service Reserved Instance offerings for a given Region. For more information, see [Reserved Instances in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ri.html).

## Request Syntax
<a name="API_DescribeReservedInstanceOfferings_RequestSyntax"></a>

```
GET /2021-01-01/opensearch/reservedInstanceOfferings?maxResults={{MaxResults}}&nextToken={{NextToken}}&offeringId={{ReservedInstanceOfferingId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeReservedInstanceOfferings_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_DescribeReservedInstanceOfferings_RequestSyntax) **   <a name="opensearchservice-DescribeReservedInstanceOfferings-request-uri-MaxResults"></a>
An optional parameter that specifies the maximum number of results to return. You can use `nextToken` to get the next page of results.
Valid Range: Maximum value of 100.

 ** [NextToken](#API_DescribeReservedInstanceOfferings_RequestSyntax) **   <a name="opensearchservice-DescribeReservedInstanceOfferings-request-uri-NextToken"></a>
If your initial `DescribeReservedInstanceOfferings` operation returns a `nextToken`, you can include the returned `nextToken` in subsequent `DescribeReservedInstanceOfferings` operations, which returns results in the next page.

 ** [ReservedInstanceOfferingId](#API_DescribeReservedInstanceOfferings_RequestSyntax) **   <a name="opensearchservice-DescribeReservedInstanceOfferings-request-uri-ReservedInstanceOfferingId"></a>
The Reserved Instance identifier filter value. Use this parameter to show only the available instance types that match the specified reservation identifier.
Length Constraints: Fixed length of 36.
Pattern: `\p{XDigit}{8}-\p{XDigit}{4}-\p{XDigit}{4}-\p{XDigit}{4}-\p{XDigit}{12}`

## Request Body
<a name="API_DescribeReservedInstanceOfferings_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeReservedInstanceOfferings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "ReservedInstanceOfferings": [
      {
         "CurrencyCode": "string",
         "Duration": number,
         "FixedPrice": number,
         "InstanceType": "string",
         "PaymentOption": "string",
         "RecurringCharges": [
            {
               "RecurringChargeAmount": number,
               "RecurringChargeFrequency": "string"
            }
         ],
         "ReservedInstanceOfferingId": "string",
         "UsagePrice": number
      }
   ]
}
```

## Response Elements
<a name="API_DescribeReservedInstanceOfferings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeReservedInstanceOfferings_ResponseSyntax) **   <a name="opensearchservice-DescribeReservedInstanceOfferings-response-NextToken"></a>
When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.
Type: String

 ** [ReservedInstanceOfferings](#API_DescribeReservedInstanceOfferings_ResponseSyntax) **   <a name="opensearchservice-DescribeReservedInstanceOfferings-response-ReservedInstanceOfferings"></a>
List of Reserved Instance offerings.
Type: Array of [ReservedInstanceOffering](API_ReservedInstanceOffering.md) objects

## Errors
<a name="API_DescribeReservedInstanceOfferings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DisabledOperationException **
An error occured because the client wanted to access an unsupported operation.
HTTP Status Code: 409

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## Examples
<a name="API_DescribeReservedInstanceOfferings_Examples"></a>

### Example
<a name="API_DescribeReservedInstanceOfferings_Example_1"></a>

This example illustrates one usage of DescribeReservedInstanceOfferings.

#### Sample Request
<a name="API_DescribeReservedInstanceOfferings_Example_1_Request"></a>

```
GET /2021-01-01/opensearch/reservedInstanceOfferings HTTP/1.1
Host: es.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.15.13 Python/3.11.6 Windows/10 exe/AMD64 prompt/off command/opensearch.describe-reserved-instance-offerings
X-Amz-Date: 20240124T220658Z
X-Amz-Security-Token: IQoJb3JpZ2luX2VjEI3wEaCXVz==
Authorization: AWS4-HMAC-SHA256 Credential=ASIAU/20240124/us-east-1/es/aws4_request, SignedHeaders=host;x-amz-date;x-amz-security-token, Signature=783312e88bf3347692920c6ad8ad623076adad31ba9163f1eeb8bc4d13f18af1
```

#### Sample Response
<a name="API_DescribeReservedInstanceOfferings_Example_1_Response"></a>

```
{
	"NextToken": "AAIAAbxp74VqN95JGZaj8LVBCCmsvixjjXg69X568WWf4AB16hLb26cZK8txZe5-JzDAB4SXGW5fOTI=",
	"ReservedInstanceOfferings": [{
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 17587.89,
		"InstanceType": "r6g.8xlarge.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.669,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "015f676e-ec97-4d63-9a5b-7f47fe4f3591",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 0.0,
		"InstanceType": "m6g.4xlarge.search",
		"PaymentOption": "NO_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.706,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "01cd94a4-8540-44b5-9cc6-a9e2121b4689",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 12811.29,
		"InstanceType": "im4gn.8xlarge.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 1.462,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "01e3d453-f2b3-4e00-8750-ef3a1af1f156",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 0.0,
		"InstanceType": "r5.12xlarge.search",
		"PaymentOption": "NO_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 2.319,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "02c3becc-bb0c-42c0-b0b3-caf3c59ee2e0",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 25703.0,
		"InstanceType": "c5.18xlarge.search",
		"PaymentOption": "ALL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.0,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "0345b77e-8f40-480c-926c-fdfa853c256b",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 13247.0,
		"InstanceType": "c5.18xlarge.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 1.512,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "03cee79c-9727-4a0d-90eb-cd76fb10236b",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 1473.0,
		"InstanceType": "c5.2xlarge.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.168,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "04c5179c-0382-4374-b583-7a6903cd9b74",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 6623.0,
		"InstanceType": "c5.9xlarge.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.756,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "066bdd2f-0012-43d4-a2c0-6f70ffecc0e0",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 1611.0,
		"InstanceType": "m5.xlarge.search",
		"PaymentOption": "ALL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.0,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "0688f67d-1085-4fbd-aca6-03739928ae52",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 6721.11,
		"InstanceType": "m6g.4xlarge.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.256,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "07027a1d-8435-4d21-80e5-4fca0804a7d0",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 0.0,
		"InstanceType": "c6g.large.search",
		"PaymentOption": "NO_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.059,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "073dbec3-4dba-49d2-9003-3ea1dc979b4f",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 0.0,
		"InstanceType": "c4.large.search",
		"PaymentOption": "NO_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.077,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "076da64d-9a9b-43b6-a1c2-236081704c59",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 11371.0,
		"InstanceType": "i3.4xlarge.search",
		"PaymentOption": "ALL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.0,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "081c153a-a3dc-401d-84c8-7837281d2c55",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 1484.82,
		"InstanceType": "c6g.xlarge.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.057,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "08784d80-853d-4b78-891c-384afbd4286c",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 0.0,
		"InstanceType": "or1.16xlarge.search",
		"PaymentOption": "NO_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 4.611,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "08e7ab36-cf38-4c89-aac3-4b81c49a1423",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 1499.581,
		"InstanceType": "m6g.2xlarge.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.171,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "097d13c1-0669-45e2-b5a9-1efc885afa2c",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 14340.996,
		"InstanceType": "im4gn.4xlarge.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.546,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "0a91faeb-75ee-4607-8edc-1fe3d715d583",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 1326.439,
		"InstanceType": "c6g.2xlarge.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.151,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "0ade739a-3ee7-4a3b-a41c-5644cf398c7e",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 9212.0,
		"InstanceType": "r4.8xlarge.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 1.052,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "0b38d87c-90fb-4fc5-969b-2520baf4b8e6",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 2509.74,
		"InstanceType": "r6gd.xlarge.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.096,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "0ce36cbf-d16e-4792-b1c4-571bb514d197",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 8934.0,
		"InstanceType": "r4.4xlarge.search",
		"PaymentOption": "ALL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.0,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "0cf79ea1-38a6-4675-8b57-3aa123f34b2b",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 0.0,
		"InstanceType": "i3.8xlarge.search",
		"PaymentOption": "NO_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 2.756,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "0df4f876-9fea-4bb0-b98d-c620e55ca8f8",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 5824.962,
		"InstanceType": "m6g.4xlarge.search",
		"PaymentOption": "ALL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.0,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "105cb1e1-dbae-4854-935c-33cd225521c8",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 0.0,
		"InstanceType": "m4.10xlarge.search",
		"PaymentOption": "NO_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 1.569,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "112f905a-29a0-49df-b21a-6324e556f6a5",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 0.0,
		"InstanceType": "r4.4xlarge.search",
		"PaymentOption": "NO_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 1.083,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "116a750e-1e71-4422-a1ea-0e8d392f5e4a",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 0.0,
		"InstanceType": "r5.4xlarge.search",
		"PaymentOption": "NO_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.773,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "11c85dc7-1545-4c83-8862-244eafd7f818",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 821.0,
		"InstanceType": "c5.large.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.031,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "1212edd1-2ee7-465b-9d4e-7d8b9c1ea30d",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 992.0,
		"InstanceType": "m4.large.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.038,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "1338aa00-2414-413a-bf40-2b09fe638675",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 4470.0,
		"InstanceType": "r4.2xlarge.search",
		"PaymentOption": "ALL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.0,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "13db2214-36dd-4c1c-b5db-5cc8abb365ea",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 0.0,
		"InstanceType": "m4.10xlarge.search",
		"PaymentOption": "NO_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 2.082,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "14677ece-7a9f-4ee4-8526-c70eb261a69c",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 0.0,
		"InstanceType": "or1.12xlarge.search",
		"PaymentOption": "NO_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 2.61,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "153e62b0-cd23-4e85-821c-f1e3f368950c",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 17423.64,
		"InstanceType": "r6gd.8xlarge.search",
		"PaymentOption": "ALL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.0,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "15b57aa7-dee6-4c0f-bc60-cbdba1851710",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 19822.0,
		"InstanceType": "m4.10xlarge.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.754,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "15fa414b-3e2e-4544-a38b-56615fa7d2b3",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 0.0,
		"InstanceType": "or1.4xlarge.search",
		"PaymentOption": "NO_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.87,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "16335325-2b2a-40f6-9363-26f8e4ec4061",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 28583.88,
		"InstanceType": "or1.12xlarge.search",
		"PaymentOption": "ALL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.0,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "16c59680-2efc-4b51-bc75-97b4c53bb07d",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 256.0,
		"InstanceType": "t3.medium.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.029,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "16f88f6e-2306-4906-85fd-2cf527c31543",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 0.0,
		"InstanceType": "r6g.2xlarge.search",
		"PaymentOption": "NO_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.462,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "18420266-f2bc-4391-9acb-72776fde40c4",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 1286.844,
		"InstanceType": "c6g.xlarge.search",
		"PaymentOption": "ALL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.0,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "1898e1d0-60d3-4804-93df-0be7e056d178",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 7713.0,
		"InstanceType": "c4.4xlarge.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.294,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "1a5c5d1f-9503-409f-a46c-9cc098bf6c4d",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 3357.27,
		"InstanceType": "m6g.2xlarge.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.128,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "1c542365-2862-4be3-9c3b-af946c152deb",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 1661.0,
		"InstanceType": "m5.2xlarge.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.19,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "1c71d96c-d7a3-4327-aa51-a44a8bed21ea",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 2444.0,
		"InstanceType": "r5.xlarge.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.093,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "1c740f32-41af-4f95-b009-cb9554b15b3f",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 1116.0,
		"InstanceType": "r4.large.search",
		"PaymentOption": "ALL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.0,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "1c95d898-f905-44a0-8a5c-678fd6e18d1b",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 79193.0,
		"InstanceType": "r4.16xlarge.search",
		"PaymentOption": "ALL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.0,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "1d3fbb87-f303-4cfa-904d-6744fcd73035",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 7405.0,
		"InstanceType": "c4.2xlarge.search",
		"PaymentOption": "ALL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.0,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "1d5a729c-cd3a-4a1f-b673-d1e44deac503",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 9972.0,
		"InstanceType": "m5.12xlarge.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 1.138,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "1d893473-bf0c-4ae3-a11e-795acbcfed0d",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 2858.0,
		"InstanceType": "c5.2xlarge.search",
		"PaymentOption": "ALL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.0,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "1d96e496-089f-4e7b-a1e2-f45de2667637",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 490.078,
		"InstanceType": "r6g.large.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.056,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "1e3258c4-015d-4c7c-9d16-d600ccd17009",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 7170.498,
		"InstanceType": "im4gn.2xlarge.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.273,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "1e665757-1104-4a31-ab6e-a9de908a3105",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 3229.286,
		"InstanceType": "m6g.xlarge.search",
		"PaymentOption": "ALL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.0,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "1ea3acb7-83f9-4461-8116-040f101c43fe",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 1190.046,
		"InstanceType": "or1.large.search",
		"PaymentOption": "ALL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.0,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "1f5d54e9-0ec9-4ca7-a87d-9b34bc04ea45",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 0.0,
		"InstanceType": "c5.2xlarge.search",
		"PaymentOption": "NO_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.261,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "1fe732c5-6cd2-4ce0-b2ba-cfd2d347eaea",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 19052.124,
		"InstanceType": "or1.8xlarge.search",
		"PaymentOption": "ALL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.0,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "1ff80eab-b0a3-4cc4-b900-c9c3fb51a4c8",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 0.0,
		"InstanceType": "m6g.xlarge.search",
		"PaymentOption": "NO_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.177,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "202bc81a-05dd-42c5-8ed1-9c6e4502dc23",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 50659.43,
		"InstanceType": "r6g.12xlarge.search",
		"PaymentOption": "ALL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.0,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "205c1007-d5a0-456e-bbc1-9308ffbbbf63",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 0.0,
		"InstanceType": "c6g.xlarge.search",
		"PaymentOption": "NO_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.156,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "2146577c-010d-4422-b03e-b5f4fee65c42",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 4604.0,
		"InstanceType": "r4.4xlarge.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.526,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "22b1be5c-1e8f-4283-b8e7-7f8ee41b1236",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 2452.8,
		"InstanceType": "or1.2xlarge.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.28,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "22f1caa7-5831-4828-83c3-2b57d4de64b6",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 0.0,
		"InstanceType": "r4.16xlarge.search",
		"PaymentOption": "NO_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 3.265,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "2340e872-66d0-44a4-8e03-7d22eb0e5895",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 40201.83,
		"InstanceType": "r6gd.16xlarge.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 1.53,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "2357617f-da8b-4eb5-a91e-9d115ed9b479",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 15425.046,
		"InstanceType": "c6g.12xlarge.search",
		"PaymentOption": "ALL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.0,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "23902774-1cba-44b0-9ac7-da616c70cc12",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 28681.992,
		"InstanceType": "im4gn.8xlarge.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 1.091,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "245da32c-86a5-4a48-9f74-77f0a41cb300",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 712.0,
		"InstanceType": "c5.large.search",
		"PaymentOption": "ALL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.0,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "24d2f163-105f-4360-8f25-2419a304c26a",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 0.0,
		"InstanceType": "r6gd.4xlarge.search",
		"PaymentOption": "NO_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.796,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "24f0be5e-513b-4b3b-bee8-ec474d8c8689",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 1907.49,
		"InstanceType": "r6g.xlarge.search",
		"PaymentOption": "ALL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.0,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "2500d63d-f25d-49c7-a028-61ec2455b874",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 840.96,
		"InstanceType": "m6g.large.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.032,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "26614ac7-2d46-4cae-afad-740d191fc788",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 5701.709,
		"InstanceType": "c6g.2xlarge.search",
		"PaymentOption": "ALL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.0,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "2682174d-11e4-44f2-bce1-b3441e19abdf",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 0.0,
		"InstanceType": "m5.large.search",
		"PaymentOption": "NO_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.098,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "26f0a787-8714-4611-8bfb-550f94e647f4",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 6001.257,
		"InstanceType": "m6g.8xlarge.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.685,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "2703ebe7-32c0-4333-942a-ccc66ee4742f",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 546.0,
		"InstanceType": "r5.large.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.062,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "270e7bdb-0954-4b32-9ffe-c79ceba20ec4",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 20104.2,
		"InstanceType": "r6gd.8xlarge.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.765,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "27386c75-5c25-4fa7-b09e-93ba6a98bdab",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 883.0,
		"InstanceType": "m4.xlarge.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.101,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "27624678-306d-4994-80e5-5831a4bd6267",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 597.87,
		"InstanceType": "or1.medium.search",
		"PaymentOption": "ALL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.0,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "2787cbb4-3900-44ac-895c-381be095eac6",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 12589.0,
		"InstanceType": "i3.2xlarge.search",
		"PaymentOption": "ALL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.0,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "289ec817-9479-4a93-87f0-b168e8e05acc",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 38053.002,
		"InstanceType": "or1.16xlarge.search",
		"PaymentOption": "ALL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.0,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "28b0e66b-e754-4907-9e37-e6c3005c2a56",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 0.0,
		"InstanceType": "m6g.4xlarge.search",
		"PaymentOption": "NO_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.532,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "29875713-058a-44e6-93e3-9e9adb2c9893",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 0.0,
		"InstanceType": "r5.2xlarge.search",
		"PaymentOption": "NO_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.513,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "29bb322a-8795-4c1a-a568-86657989a31e",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 7624.266,
		"InstanceType": "r6g.4xlarge.search",
		"PaymentOption": "ALL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.0,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "2a5013f1-9a4a-4378-ac10-d529dc71136c",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 575.0,
		"InstanceType": "r4.large.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.066,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "2ae48c42-c556-43e4-af03-af472b3d579f",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 0.0,
		"InstanceType": "r5.12xlarge.search",
		"PaymentOption": "NO_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 3.077,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "2b3098fc-7fec-4bb8-8f7b-43e454c5be78",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 10052.1,
		"InstanceType": "r6gd.4xlarge.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.383,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "2b7743ec-ce93-4ae1-827d-83192cba0610",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 10545.638,
		"InstanceType": "or1.2xlarge.search",
		"PaymentOption": "ALL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.0,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "2bdc713e-7240-4b26-82f7-986294e5c489",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 1087.554,
		"InstanceType": "r6gd.large.search",
		"PaymentOption": "ALL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.0,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "2ccd9263-7d0e-4e83-b70b-8f0a259a881a",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 39597.0,
		"InstanceType": "r4.8xlarge.search",
		"PaymentOption": "ALL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.0,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "2d995bb3-00bd-4924-ba5a-aa50630506b6",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 1097.19,
		"InstanceType": "r6g.large.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.042,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "2e380e6e-130b-4cfb-8da3-e458defba6f6",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 2244.969,
		"InstanceType": "r6gd.2xlarge.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.256,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "2ee4c7c1-f162-40e8-91b9-6a015409f6a2",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 5285.434,
		"InstanceType": "or1.xlarge.search",
		"PaymentOption": "ALL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.0,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "2f36cb75-ef17-4ce2-9082-8b48dd3fd9e9",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 0.0,
		"InstanceType": "r4.xlarge.search",
		"PaymentOption": "NO_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.204,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "2f36f1af-4a75-4736-b4d2-c96c747c0f09",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 0.0,
		"InstanceType": "i3.xlarge.search",
		"PaymentOption": "NO_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.259,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "2fa008d1-6f07-4f6a-8602-56c0b24ee8a1",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 0.0,
		"InstanceType": "m6g.large.search",
		"PaymentOption": "NO_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.067,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "314ab470-5920-4efb-9ceb-12c3fe3b14ac",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 1425.427,
		"InstanceType": "c6g.large.search",
		"PaymentOption": "ALL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.0,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "317dfe20-f11d-4524-97cd-360c09f6caa6",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 1859.0,
		"InstanceType": "m5.xlarge.search",
		"PaymentOption": "PARTIAL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.071,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "32215331-1366-4bed-bd07-f345ad3a24eb",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 6685.0,
		"InstanceType": "c4.4xlarge.search",
		"PaymentOption": "ALL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.0,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "32977df3-b9a3-48b2-af6d-1cd6dc64902d",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 1614.643,
		"InstanceType": "m6g.large.search",
		"PaymentOption": "ALL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.0,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "32a8e2e4-877c-49bb-aca2-8ac004783acb",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 22781.606,
		"InstanceType": "c6g.8xlarge.search",
		"PaymentOption": "ALL_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.0,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "3559397a-10cc-4e30-a8e8-8c105cd2572c",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 0.0,
		"InstanceType": "r6gd.16xlarge.search",
		"PaymentOption": "NO_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 4.222,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "35d3c0cc-d935-4847-96f5-240149fd35e3",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 0.0,
		"InstanceType": "m6g.2xlarge.search",
		"PaymentOption": "NO_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.353,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "3612dd00-b132-43ee-adb8-71666412ca89",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 0.0,
		"InstanceType": "c6g.8xlarge.search",
		"PaymentOption": "NO_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 1.246,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "361ad9aa-d816-4de5-a5a5-8a129558a1da",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 31536000,
		"FixedPrice": 0.0,
		"InstanceType": "c5.2xlarge.search",
		"PaymentOption": "NO_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.346,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "365cfbb6-2d5c-4973-ad73-b511cebe907a",
		"UsagePrice": 0.0
	}, {
		"CurrencyCode": "USD",
		"Duration": 94608000,
		"FixedPrice": 0.0,
		"InstanceType": "c5.large.search",
		"PaymentOption": "NO_UPFRONT",
		"RecurringCharges": [{
			"RecurringChargeAmount": 0.065,
			"RecurringChargeFrequency": "Hourly"
		}],
		"ReservedInstanceOfferingId": "36b7e031-8778-421a-9eb3-232ddfc14ef6",
		"UsagePrice": 0.0
	}]
}
```

## See Also
<a name="API_DescribeReservedInstanceOfferings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/DescribeReservedInstanceOfferings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/DescribeReservedInstanceOfferings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DescribeReservedInstanceOfferings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/DescribeReservedInstanceOfferings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DescribeReservedInstanceOfferings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/DescribeReservedInstanceOfferings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/DescribeReservedInstanceOfferings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/DescribeReservedInstanceOfferings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/DescribeReservedInstanceOfferings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DescribeReservedInstanceOfferings)
