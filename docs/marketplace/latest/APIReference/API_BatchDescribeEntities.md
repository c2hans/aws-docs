---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_BatchDescribeEntities.html
---

# BatchDescribeEntities
<a name="API_BatchDescribeEntities"></a>

Returns metadata and content for multiple entities. This is the Batch version of the `DescribeEntity` API and uses the same IAM permission action as `DescribeEntity` API.

## Request Syntax
<a name="API_BatchDescribeEntities_RequestSyntax"></a>

```
POST /BatchDescribeEntities HTTP/1.1
Content-type: application/json

{
   "EntityRequestList": [
      {
         "Catalog": "{{string}}",
         "EntityId": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchDescribeEntities_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchDescribeEntities_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [EntityRequestList](#API_BatchDescribeEntities_RequestSyntax) **   <a name="AWSMarketplaceService-BatchDescribeEntities-request-EntityRequestList"></a>
List of entity IDs and the catalogs the entities are present in.
Type: Array of [EntityRequest](API_EntityRequest.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: Yes

## Response Syntax
<a name="API_BatchDescribeEntities_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EntityDetails": {
      "string" : {
         "DetailsDocument": JSON value,
         "EntityArn": "string",
         "EntityIdentifier": "string",
         "EntityType": "string",
         "LastModifiedDate": "string"
      }
   },
   "Errors": {
      "string" : {
         "ErrorCode": "string",
         "ErrorMessage": "string"
      }
   }
}
```

## Response Elements
<a name="API_BatchDescribeEntities_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EntityDetails](#API_BatchDescribeEntities_ResponseSyntax) **   <a name="AWSMarketplaceService-BatchDescribeEntities-response-EntityDetails"></a>
Details about each entity.
Type: String to [EntityDetail](API_EntityDetail.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `^[a-zA-Z0-9][.a-zA-Z0-9/-]+[a-zA-Z0-9]$`

 ** [Errors](#API_BatchDescribeEntities_ResponseSyntax) **   <a name="AWSMarketplaceService-BatchDescribeEntities-response-Errors"></a>
A map of errors returned, with `EntityId` as the key and `errorDetail` as the value.
Type: String to [BatchDescribeErrorDetail](API_BatchDescribeErrorDetail.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `^[a-zA-Z0-9][.a-zA-Z0-9/-]+[a-zA-Z0-9]$`

## Errors
<a name="API_BatchDescribeEntities_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP status code: 403
HTTP Status Code: 403

 ** InternalServiceException **
There was an internal service exception.
HTTP status code: 500
HTTP Status Code: 500

 ** ThrottlingException **
Too many requests.
HTTP status code: 429
HTTP Status Code: 429

 ** ValidationException **
An error occurred during validation.
HTTP status code: 422
HTTP Status Code: 422

## Examples
<a name="API_BatchDescribeEntities_Examples"></a>

### Sample request for SaaS products
<a name="API_BatchDescribeEntities_Example_1"></a>

You can use `BatchDescribeEntities` to obtain information about multiple software as a service (SaaS) products at the same time. The examples below show how to obtain details on two products at the same time and how the response looks like when one product exists and another one does not.

```
{
    "EntityRequestList": [
        { "EntityId": "example-123-abcd", "Catalog": "AWSMarketplace"},
        { "EntityId": "example-456-abcd", "Catalog": "AWSMarketplace"}
    ]
}
```

### Sample response for SaaS products
<a name="API_BatchDescribeEntities_Example_2"></a>

This example illustrates one usage of BatchDescribeEntities.

```
{
    "EntityDetails": {
        "example-123-abcd": {
            "EntityArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/SaaSProduct/example-123-abcd",
            "EntityType": "SaaSProduct@1.0",
            "EntityIdentifier": "example-123-abcd@1",
            "LastModifiedDate": "2023-07-31T20:37:08Z",
            "DetailsDocument": {
                "Description": {
                    "ProductTitle": "Test title",
                    "ProductCode": "prod-example123",
                    "ShortDescription": "Test description",
                    "Manufacturer": "TeamExtension",
                    "LongDescription": "The full description.",
                    "Sku": null,
                    "Highlights": [
                        "test highlights"
                    ],
                    "AssociatedProducts": null,
                    "SearchKeywords": [
                        "Configuration file management"
                    ],
                    "Visibility": "Limited",
                    "ProductState": "Active",
                    "Categories": [
                        "Security"
                    ]
                },
                "PromotionalResources": {
                    "LogoUrl": "http://awsmp-logos.s3.amazonaws.com/11267590-efc3-4be5-b1b2-7e461e1dd2c6_config_Logo.png",
                    "Videos": [],
                    "AdditionalResources": [
                        {
                            "Type": "Link",
                            "Text": "Manage your configuration files with ease",
                            "Url": "http://www.configapp.com/post/category/tutorials/"
                        }
                    ],
                    "PromotionalMedia": null
                },
                "SupportInformation": {
                    "Description": "Site tutorials, mail and direct contact details",
                    "Resources": []
                },
                "Dimensions": [
                    {
                        "Name": "Starter Plan",
                        "Description": "Starter Plan",
                        "Key": "StarterPlan",
                        "Unit": "Mbps",
                        "Types": [
                            "ExternallyMetered"
                        ]
                    }
                ],
                "Versions": [
                    {
                        "Id": "version-123",
                        "DeliveryOptions": [
                            {
                                "Id": "do-hg5tfkwp2vxqi",
                                "Type": "SoftwareRegistration",
                                "FulfillmentUrl": ""
                            }
                        ]
                    }
                ],
                "Targeting": {
                    "PositiveTargeting": {
                        "BuyerAccounts": [
                            "123456789012"
                        ]
                    }
                }
            },
        }
    },
     "Errors": {
        "example-456-abcd": {
            "ErrorCode": "ResourceNotFound",
            "ErrorMessage": "Requested entity 'example-456-abcd' does not exist."
        }
    }
}
```

### Sample request for offer entities
<a name="API_BatchDescribeEntities_Example_3"></a>

You can use `BatchDescribeEntities` to obtain information about multiple offers at once. The examples below show how to obtain details on two offers at the same time.

```
{
    "EntityRequestList": [
        { "EntityId": "offer-example123", "Catalog": "AWSMarketplace"},
        { "EntityId": "offer-example456", "Catalog": "AWSMarketplace"}
    ]
}
```

### Sample response for offer entities
<a name="API_BatchDescribeEntities_Example_4"></a>

This example illustrates one usage of BatchDescribeEntities.

```
{
    "EntityDetails": {
        "offer-example123": {
            "EntityArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/Offer/offer-example123",
            "EntityType": "Offer@1.0",
            "EntityIdentifier": "offer-example123@1",
            "LastModifiedDate": "2023-07-31T20:37:08Z",
            "DetailsDocument": {
                "Id": "offer-example123",
                "State": "Released",
                "Name": "Test Offer",
                "Description": "Worldwide offer for Test Product",
                "PreExistingAgreement": {
                "AcquisitionChannel": "External",
                "PricingModel": "Contract"
                },
                "ProductId": "prod-example123",
                "Terms": [
                {
                    "Type": "SupportTerm",
                    "RefundPolicy": "If you need to request a refund for software sold by Amazon Web Services, LLC, please contact AWS Customer Service."
                },
                {
                    "Type": "LegalTerm",
                    "Documents": [
                    {
                        "Type": "CustomEula",
                        "Url": "https://s3.amazonaws.com/EULA/custom-eula-1234.txt"
                    }
                    ]
                },
                {
                    "Type": "FreeTrialPricingTerm",
                    "Duration": "P30D",
                    "Grants": [
                    {
                        "DimensionKey": "m3.xlarge",
                        "MaxQuantity": 10
                    },
                    {
                        "DimensionKey": "m4.xlarge",
                        "MaxQuantity": 10
                    }
                    ]
                },
                {
                    "Type": "ConfigurableUpfrontPricingTerm",
                    "CurrencyCode": "USD",
                    "RateCards": [
                    {
                        "Selector": {
                        "Type": "Duration",
                        "Value": "P365D"
                        },
                        "RateCard": [
                        {
                            "DimensionKey": "m3.large",
                            "Price": "300.00"
                        },
                        {
                            "DimensionKey": "m4.xlarge",
                            "Price": "400.00"
                        }
                        ],
                        "Constraints": {
                        "MultipleDimensionSelection": "Allowed",
                        "QuantityConfiguration": "Allowed"
                        }
                    }
                    ]
                },
                {
                    "Type": "UsageBasedPricingTerm",
                    "CurrencyCode": "USD",
                    "RateCards": [
                    {
                        "RateCard": [
                        {
                            "DimensionKey": "m3.large",
                            "Price": "0.10"
                        },
                        {
                            "DimensionKey": "m4.xlarge",
                            "Price": "0.20"
                        }
                        ]
                    }
                    ]
                },
                {
                    "Type": "FixedUpfrontPricingTerm",
                    "CurrencyCode": "USD",
                    "Price": "200.00",
                    "Grants": [
                    {
                        "DimensionKey": "Users",
                        "MaxQuantity": 10
                    }
                    ]
                },
                {
                    "Type": "RecurringPaymentTerm",
                    "CurrencyCode": "USD",
                    "BillingPeriod": "Monthly",
                    "Price": "100.0"
                },
                {
                    "Type": "PaymentScheduleTerm",
                    "CurrencyCode": "USD",
                    "Schedule": [
                    {
                        "ChargeDate": "2020-12-01T00:00:00.000Z",
                        "ChargeAmount": "1000.00"
                    },
                    {
                        "ChargeDate": "2021-06-15T00:00:00.000Z",
                        "ChargeAmount": "1250.00"
                    }
                    ]
                },
                {
                    "Type": "ByolPricingTerm"
                },
                {
                    "Type": "RenewalTerm"
                }
                ],
                "Rules": [
                {
                    "Type": "TargetingRule",
                    "PositiveTargeting": {
                    "CountryCodes": [
                        "US",
                        "CA"
                    ],
                    "BuyerAccounts": [
                        "123456789012"
                    ]
                    },
                    "NegativeTargeting": {
                    "CountryCodes": [
                        "XX"
                    ]
                    }
                },
                {
                    "Type": "AvailabilityRule",
                    "AvailabilityEndDate": "2024-08-30T01:56:03.000Z"
                }
                ]
            }
        },
        "offer-example456": {
            "EntityArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/Offer/offer-example456",
            "EntityType": "Offer@1.0",
            "EntityIdentifier": "offer-example456@1",
            "LastModifiedDate": "2023-07-31T21:37:08Z",
            "DetailsDocument": {
                "Id": "offer-example456",
                "State": "Released",
                "Name": "Test Offer",
                "Description": "Worldwide offer for Test Product",
                "PreExistingAgreement": {
                "AcquisitionChannel": "External",
                "PricingModel": "Contract"
                },
                "ProductId": "prod-example456",
                "Terms": [
                {
                    "Type": "SupportTerm",
                    "RefundPolicy": "If you need to request a refund for software sold by Amazon Web Services, LLC, please contact AWS Customer Service."
                },
                {
                    "Type": "LegalTerm",
                    "Documents": [
                    {
                        "Type": "CustomEula",
                        "Url": "https://s3.amazonaws.com/EULA/custom-eula-1234.txt"
                    }
                    ]
                },
                {
                    "Type": "FreeTrialPricingTerm",
                    "Duration": "P30D",
                    "Grants": [
                    {
                        "DimensionKey": "m3.xlarge",
                        "MaxQuantity": 10
                    },
                    {
                        "DimensionKey": "m4.xlarge",
                        "MaxQuantity": 10
                    }
                    ]
                },
                {
                    "Type": "ConfigurableUpfrontPricingTerm",
                    "CurrencyCode": "USD",
                    "RateCards": [
                    {
                        "Selector": {
                        "Type": "Duration",
                        "Value": "P365D"
                        },
                        "RateCard": [
                        {
                            "DimensionKey": "m3.large",
                            "Price": "300.00"
                        },
                        {
                            "DimensionKey": "m4.xlarge",
                            "Price": "400.00"
                        }
                        ],
                        "Constraints": {
                        "MultipleDimensionSelection": "Allowed",
                        "QuantityConfiguration": "Allowed"
                        }
                    }
                    ]
                },
                {
                    "Type": "UsageBasedPricingTerm",
                    "CurrencyCode": "USD",
                    "RateCards": [
                    {
                        "RateCard": [
                        {
                            "DimensionKey": "m3.large",
                            "Price": "0.10"
                        },
                        {
                            "DimensionKey": "m4.xlarge",
                            "Price": "0.20"
                        }
                        ]
                    }
                    ]
                },
                {
                    "Type": "FixedUpfrontPricingTerm",
                    "CurrencyCode": "USD",
                    "Price": "200.00",
                    "Grants": [
                    {
                        "DimensionKey": "Users",
                        "MaxQuantity": 10
                    }
                    ]
                },
                {
                    "Type": "RecurringPaymentTerm",
                    "CurrencyCode": "USD",
                    "BillingPeriod": "Monthly",
                    "Price": "100.0"
                },
                {
                    "Type": "PaymentScheduleTerm",
                    "CurrencyCode": "USD",
                    "Schedule": [
                    {
                        "ChargeDate": "2020-12-01T00:00:00.000Z",
                        "ChargeAmount": "1000.00"
                    },
                    {
                        "ChargeDate": "2021-06-15T00:00:00.000Z",
                        "ChargeAmount": "1250.00"
                    }
                    ]
                },
                {
                    "Type": "ByolPricingTerm"
                },
                {
                    "Type": "RenewalTerm"
                }
                ],
                "Rules": [
                {
                    "Type": "TargetingRule",
                    "PositiveTargeting": {
                    "CountryCodes": [
                        "US",
                        "CA"
                    ],
                    "BuyerAccounts": [
                        "123456789012"
                    ]
                    },
                    "NegativeTargeting": {
                    "CountryCodes": [
                        "XX"
                    ]
                    }
                },
                {
                    "Type": "AvailabilityRule",
                    "AvailabilityEndDate": "2024-08-30T01:56:03.000Z"
                }
                ]
            }
        },
        }
    }
}
```

### Sample request for resale authorization entities
<a name="API_BatchDescribeEntities_Example_5"></a>

You can use `BatchDescribeEntities` to obtain information on multiple resale authorizations at once. The examples below show how to obtain details on two resale authorizations at the same time.

```
{
    "EntityRequestList": [
        { "EntityId": "resaleauthz-example123", "Catalog": "AWSMarketplace"},
        { "EntityId": "resaleauthz-example456", "Catalog": "AWSMarketplace"}
    ]
}
```

### Sample response for resale authorization entities
<a name="API_BatchDescribeEntities_Example_6"></a>

This example illustrates one usage of BatchDescribeEntities.

```
{
    "EntityDetails": {
        "resaleauthz-example123": {
            "EntityArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ResaleAuthorization/resaleauthz-example123",
            "EntityType": "ResaleAuthorization@1.0",
            "EntityIdentifier": "resaleauthz-example123@1",
            "LastModifiedDate": "2023-07-31T20:37:08Z",
            "DetailsDocument": {
                "Name": "TestResaleAuthorization",
                "Description": "ResaleAuthorization for Test Product",
                "ProductId": "prod-example123",
                "ProductName": "TestProduct",
                "Status": "Active",
                "PreExistingBuyerAgreement": {
                "AcquisitionChannel": "Unknown",
                "PricingModel": "Unknown"
                },
                "CreatedDate": "2023-07-18T16:39:31.335Z",
                "ManufacturerLegalName": "ChannelCAPI.Inc",
                "ManufacturerAccountId": "123456789012",
                "Dimensions": [
                {
                    "Name": "Protected Resources",
                    "Description": "Additional 100 protected resources",
                    "Key": "hundredresources",
                    "Unit": "Units",
                    "Types": [
                    "Entitled"
                    ]
                }
                ],
                "OfferDetails": {
                "OfferExtendedStatus": "Not Started",
                "OfferCreatedCount": 0
                },
                "Terms": [
                {
                    "Type": "ResaleUsageBasedPricingTerm",
                    "Id": "term_id_placeholder",
                    "CurrencyCode": "USD",
                    "RateCards": [
                    {
                        "RateCard": [
                        {
                            "DimensionKey": "resource_number",
                            "Price": "0.05"
                        },
                        {
                            "DimensionKey": "scanned_data",
                            "Price": "0.05"
                        }
                        ]
                    }
                    ]
                },
                {
                    "Type": "ResaleConfigurableUpfrontPricingTerm",
                    "Id": "term_id_placeholder",
                    "CurrencyCode": "USD",
                    "RateCards": [
                    {
                        "Selector": {
                        "Type": "Duration",
                        "Value": "P24M"
                        },
                        "RateCard": [
                        {
                            "DimensionKey": "hundredresources",
                            "Price": "0.04"
                        },
                        {
                            "DimensionKey": "tenTBData",
                            "Price": "0.03"
                        },
                        {
                            "DimensionKey": "channel_custom",
                            "Price": "0.02"
                        }
                        ],
                        "Constraints": {
                        "MultipleDimensionSelection": "Allowed",
                        "QuantityConfiguration": "Allowed"
                        }
                    }
                    ]
                },
                {
                    "Type": "ResaleFixedUpfrontPricingTerm",
                    "Id": "term-123",
                    "CurrencyCode": "USD",
                    "Duration": "P180D",
                    "Price": "0.0",
                    "Grants": [
                    {
                        "DimensionKey": "example1230xm1",
                        "MaxQuantity": 1
                    }
                    ]
                },
                {
                    "Type": "ResalePaymentScheduleTerm",
                    "Id": "term-123",
                    "CurrencyCode": "USD",
                    "Schedule": [
                    {
                        "ChargeDate": "2018-07-01T00:00:00.000Z",
                        "ChargeAmount": "200.00"
                    },
                    {
                        "ChargeDate": "2019-05-01T00:00:00.000Z",
                        "ChargeAmount": "200.00"
                    }
                    ]
                },
                {
                    "Type": "BuyerLegalTerm",
                    "Id": "term_id_placeholder",
                    "Documents": [
                    {
                        "Type": "StandardEula",
                        "Url": "https://s3.amazonaws.com/EULA/custom-eula-1234.txt"
                    }
                    ]
                },
                {
                    "Type": "ResaleLegalTerm",
                    "Id": "term_id_placeholder",
                    "Documents": [
                    {
                        "Type": "StandardResellerContract",
                        "Url": "https://s3.amazonaws.com/EULA/custom-eula-1234.txt"
                    }
                    ]
                },
                {
                    "Type": "BuyerValidityTerm",
                    "Id": "term_id_placeholder",
                    "MaximumAgreementStartDate": "2023-09-25T23:59:59.000Z"
                },
                {
                    "Type": "BuyerTargetingTerm",
                    "Id": "term_id_placeholder",
                    "PositiveTargeting": {
                    "BuyerAccounts": [
                        {
                        "AwsAccountId": "123456789012"
                        }
                    ]
                    }
                }
                ],
                "Rules": [
                {
                    "Type": "AvailabilityRule",
                    "Id": "availability_rule_id_placeholder",
                    "Usage": "Limited",
                    "AvailabilityEndDate": "2024-05-31T23:59:59Z",
                    "OffersMaxQuantity": 1
                },
                {
                    "Type": "PartnerTargetingRule",
                    "Id": "partner_targeting_rule_id_placeholder",
                    "ResellerAccountId": "123456789012",
                    "ResellerLegalName": "ChannelCAPICP.Inc",
                    "ResellerRole": "ChannelPartner"
                }
                ]
            }
        },
        "resaleauthz-example456": {
            "EntityArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ResaleAuthorization/resaleauthz-example456",
            "EntityType": "ResaleAuthorization@1.0",
            "EntityIdentifier": "resaleauthz-example456@1",
            "LastModifiedDate": "2023-07-31T22:37:08Z",
            "DetailsDocument": {
                "Name": "TestResaleAuthorization",
                "Description": "ResaleAuthorization for Test Product",
                "ProductId": "prod-example456",
                "ProductName": "TestProduct",
                "Status": "Active",
                "PreExistingBuyerAgreement": {
                "AcquisitionChannel": "Unknown",
                "PricingModel": "Unknown"
                },
                "CreatedDate": "2023-07-18T16:39:31.335Z",
                "ManufacturerLegalName": "ChannelCAPI.Inc",
                "ManufacturerAccountId": "123456789012",
                "Dimensions": [
                {
                    "Name": "Protected Resources",
                    "Description": "Additional 100 protected resources",
                    "Key": "hundredresources",
                    "Unit": "Units",
                    "Types": [
                    "Entitled"
                    ]
                }
                ],
                "OfferDetails": {
                "OfferExtendedStatus": "Not Started",
                "OfferCreatedCount": 0
                },
                "Terms": [
                {
                    "Type": "ResaleUsageBasedPricingTerm",
                    "Id": "term_id_placeholder",
                    "CurrencyCode": "USD",
                    "RateCards": [
                    {
                        "RateCard": [
                        {
                            "DimensionKey": "resource_number",
                            "Price": "0.05"
                        },
                        {
                            "DimensionKey": "scanned_data",
                            "Price": "0.05"
                        }
                        ]
                    }
                    ]
                },
                {
                    "Type": "ResaleConfigurableUpfrontPricingTerm",
                    "Id": "term_id_placeholder",
                    "CurrencyCode": "USD",
                    "RateCards": [
                    {
                        "Selector": {
                        "Type": "Duration",
                        "Value": "P24M"
                        },
                        "RateCard": [
                        {
                            "DimensionKey": "hundredresources",
                            "Price": "0.04"
                        },
                        {
                            "DimensionKey": "tenTBData",
                            "Price": "0.03"
                        },
                        {
                            "DimensionKey": "channel_custom",
                            "Price": "0.02"
                        }
                        ],
                        "Constraints": {
                        "MultipleDimensionSelection": "Allowed",
                        "QuantityConfiguration": "Allowed"
                        }
                    }
                    ]
                },
                {
                    "Type": "ResaleFixedUpfrontPricingTerm",
                    "Id": "term-123",
                    "CurrencyCode": "USD",
                    "Duration": "P180D",
                    "Price": "0.0",
                    "Grants": [
                    {
                        "DimensionKey": "example1230xm1",
                        "MaxQuantity": 1
                    }
                    ]
                },
                {
                    "Type": "ResalePaymentScheduleTerm",
                    "Id": "term-123",
                    "CurrencyCode": "USD",
                    "Schedule": [
                    {
                        "ChargeDate": "2018-07-01T00:00:00.000Z",
                        "ChargeAmount": "200.00"
                    },
                    {
                        "ChargeDate": "2019-05-01T00:00:00.000Z",
                        "ChargeAmount": "200.00"
                    }
                    ]
                },
                {
                    "Type": "BuyerLegalTerm",
                    "Id": "term_id_placeholder",
                    "Documents": [
                    {
                        "Type": "StandardEula",
                        "Url": "https://s3.amazonaws.com/EULA/custom-eula-1234.txt"
                    }
                    ]
                },
                {
                    "Type": "ResaleLegalTerm",
                    "Id": "term_id_placeholder",
                    "Documents": [
                    {
                        "Type": "StandardResellerContract",
                        "Url": "https://s3.amazonaws.com/EULA/custom-eula-1234.txt"
                    }
                    ]
                },
                {
                    "Type": "BuyerValidityTerm",
                    "Id": "term_id_placeholder",
                    "MaximumAgreementStartDate": "2023-09-25T23:59:59.000Z"
                },
                {
                    "Type": "BuyerTargetingTerm",
                    "Id": "term_id_placeholder",
                    "PositiveTargeting": {
                    "BuyerAccounts": [
                        {
                        "AwsAccountId": "123456789012"
                        }
                    ]
                    }
                }
                ],
                "Rules": [
                {
                    "Type": "AvailabilityRule",
                    "Id": "availability_rule_id_placeholder",
                    "Usage": "Limited",
                    "AvailabilityEndDate": "2024-05-31T23:59:59Z",
                    "OffersMaxQuantity": 1
                },
                {
                    "Type": "PartnerTargetingRule",
                    "Id": "partner_targeting_rule_id_placeholder",
                    "ResellerAccountId": "123456789012",
                    "ResellerLegalName": "ChannelCAPICP.Inc",
                    "ResellerRole": "Distributor"
                }
                ]
            }
        }
    }
}
```

## See Also
<a name="API_BatchDescribeEntities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-catalog-2018-09-17/BatchDescribeEntities)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-catalog-2018-09-17/BatchDescribeEntities)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/BatchDescribeEntities)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-catalog-2018-09-17/BatchDescribeEntities)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/BatchDescribeEntities)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-catalog-2018-09-17/BatchDescribeEntities)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-catalog-2018-09-17/BatchDescribeEntities)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-catalog-2018-09-17/BatchDescribeEntities)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/marketplace-catalog-2018-09-17/BatchDescribeEntities)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/BatchDescribeEntities)
