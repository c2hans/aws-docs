---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/marketplace-agreement_example_marketplace-agreement_DescribeAgreement_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Get information about an agreement using an AWS SDK
<a name="marketplace-agreement_example_marketplace-agreement_DescribeAgreement_section"></a>

The following code examples show how to get information about an agreement.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/java#agreement-api-reference-code) repository.

```
package com.example.awsmarketplace.agreementapi.seller;

import static com.example.awsmarketplace.utils.ReferenceCodesConstants.*;
import com.example.awsmarketplace.utils.ReferenceCodesUtils;

import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.services.marketplaceagreement.MarketplaceAgreementClient;
import software.amazon.awssdk.services.marketplaceagreement.model.DescribeAgreementRequest;
import software.amazon.awssdk.services.marketplaceagreement.model.DescribeAgreementResponse;

public class DescribeAgreement {

	public static void main(String[] args) {

		String agreementId = args.length > 0 ? args[0] : AGREEMENT_ID;

		DescribeAgreementResponse describeAgreementResponse = getResponse(agreementId);

		ReferenceCodesUtils.formatOutput(describeAgreementResponse);

	}

	public static DescribeAgreementResponse getResponse(String agreementId) {
		MarketplaceAgreementClient marketplaceAgreementClient =
				MarketplaceAgreementClient.builder()
				.httpClient(ApacheHttpClient.builder().build())
				.credentialsProvider(ProfileCredentialsProvider.create())
				.build();

		DescribeAgreementRequest describeAgreementRequest =
				DescribeAgreementRequest.builder()
				.agreementId(agreementId)
				.build();

		DescribeAgreementResponse describeAgreementResponse = marketplaceAgreementClient.describeAgreement(describeAgreementRequest);
		return describeAgreementResponse;
	}

}
```
+  For API details, see [DescribeAgreement](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/DescribeAgreement) in *AWS SDK for Java 2.x API Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/blob/main/python#agreement-api-reference-code) repository.

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Purpose
Shows how to use the AWS SDK for Python (Boto3) to get agreement information
AG-07
"""

import argparse
import logging

import boto3
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

import utils.helpers as helper
from botocore.exceptions import ClientError

mp_client = boto3.client("marketplace-agreement")

logger = logging.getLogger(__name__)

def get_agreement_information(agreement_id):
    try:
        response = mp_client.describe_agreement(agreementId=agreement_id)
    except ClientError as e:
        if e.response["Error"]["Code"] == "ResourceNotFoundException":
            logger.error("Agreement with ID %s not found.", agreement_id)
            raise e
        else:
            logger.error("Unexpected error: %s", e)
            raise e

    return response

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--agreement-id",
        "-aid",
        help="Provide agreement ID to describe agreement status",
        required=True,
    )
    args = parser.parse_args()

    response = get_agreement_information(agreement_id=args.agreement_id)

    helper.pretty_print_datetime(response)
```
+  For API details, see [DescribeAgreement](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/DescribeAgreement) in *AWS SDK for Python (Boto3) API Reference*.

------
