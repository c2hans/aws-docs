---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cli_2_service-catalog_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Service Catalog examples using AWS CLI
<a name="cli_2_service-catalog_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Service Catalog.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `accept-portfolio-share`
<a name="service-catalog_AcceptPortfolioShare_cli_2_topic"></a>

The following code example shows how to use `accept-portfolio-share`.

**AWS CLI**
**To accept a portfolio share**
The following `accept-portfolio-share` example accepts an offer, made by another user, to share the specified portfolio.

```
aws servicecatalog accept-portfolio-share \
    --portfolio-id {{port-2s6wuabcdefghijk}}
```
This command produces no output.
+  For API details, see [AcceptPortfolioShare](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/accept-portfolio-share.html) in *AWS CLI Command Reference*.

### `associate-principal-with-portfolio`
<a name="service-catalog_AssociatePrincipalWithPortfolio_cli_2_topic"></a>

The following code example shows how to use `associate-principal-with-portfolio`.

**AWS CLI**
**To associate a principal with a portfolio**
The following `associate-principal-with-portfolio` example associates a user with the specified portfolio.

```
aws servicecatalog associate-principal-with-portfolio \
    --portfolio-id {{port-2s6abcdefwdh4}} \
    --principal-arn {{arn:aws:iam::123456789012:user/usertest}} \
    --principal-type {{IAM}}
```
This command produces no output.
+  For API details, see [AssociatePrincipalWithPortfolio](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/associate-principal-with-portfolio.html) in *AWS CLI Command Reference*.

### `associate-product-with-portfolio`
<a name="service-catalog_AssociateProductWithPortfolio_cli_2_topic"></a>

The following code example shows how to use `associate-product-with-portfolio`.

**AWS CLI**
**To associate a product with a portfolio**
The following `associate-product-with-portfolio` example associates the given product with the specified portfolio.

```
aws servicecatalog associate-product-with-portfolio
     --product-id {{prod-3p5abcdef3oyk}}
     --portfolio-id {{port-2s6abcdef5wdh4}}
```
This command produces no output.
+  For API details, see [AssociateProductWithPortfolio](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/associate-product-with-portfolio.html) in *AWS CLI Command Reference*.

### `associate-tag-option-with-resource`
<a name="service-catalog_AssociateTagOptionWithResource_cli_2_topic"></a>

The following code example shows how to use `associate-tag-option-with-resource`.

**AWS CLI**
**To associate a TagOption with a resource**
The following `associate-tag-option-with-resource` example associates the specified TagOption with the specified resource.

```
aws servicecatalog associate-tag-option-with-resource \
    --resource-id {{port-2s6abcdq5wdh4}} \
    --tag-option-id {{tag-p3abc2pkpz5qc}}
```
This command produces no output.
+  For API details, see [AssociateTagOptionWithResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/associate-tag-option-with-resource.html) in *AWS CLI Command Reference*.

### `copy-product`
<a name="service-catalog_CopyProduct_cli_2_topic"></a>

The following code example shows how to use `copy-product`.

**AWS CLI**
**To copy a product**
The following `copy-product` example makes a copy of the specified product, using a JSON file to pass parameters.

```
aws servicecatalog copy-product --cli-input-json {{file://copy-product-input.json}}
```
Contents of `copy-product-input.json`:

```
{
    "SourceProductArn": "arn:aws:catalog:us-west-2:123456789012:product/prod-tcabcd3syn2xy",
    "TargetProductName": "copy-of-myproduct",
    "CopyOptions": [
        "CopyTags"
    ]
}
```
Output:

```
{
    "CopyProductToken": "copyproduct-abc5defgjkdji"
}
```
+  For API details, see [CopyProduct](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/copy-product.html) in *AWS CLI Command Reference*.

### `create-constraint`
<a name="service-catalog_CreateConstraint_cli_2_topic"></a>

The following code example shows how to use `create-constraint`.

**AWS CLI**
**To create a constraints**
The following `create-constraint` example creates a constraint.

```
aws servicecatalog create-constraint \
    --portfolio-id {{port-y3fnkesxxxxx}} \
    --product-id {{prod-cfrfxmraxxxxx}} \
    --type {{LAUNCH}} \
    --parameters '{{{"RoleArn" : "arn:aws:iam::123456789012:role/LaunchRole"}}}'
```
Output:

```
{
    "ConstraintDetail": {
        "ConstraintId": "cons-7tr6gei4bxxxx",
        "Type": "LAUNCH",
        "Owner": "123456789012",
        "ProductId": "prod-cfrfxmra3xxxx",
        "PortfolioId": "port-y3fnkeslpxxxx"
    },
    "ConstraintParameters": "{\"RoleArn\" : \"arn:aws:iam::123456789012:role/LaunchRole\"}",
    "Status": "CREATING"
}
```
For more information, see [Using AWS Service Catalog Constraints](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/constraints.html) in the *AWS Service Catalog User Guide*.
+  For API details, see [CreateConstraint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/create-constraint.html) in *AWS CLI Command Reference*.

### `create-portfolio-share`
<a name="service-catalog_CreatePortfolioShare_cli_2_topic"></a>

The following code example shows how to use `create-portfolio-share`.

**AWS CLI**
**To share a portfolio with an account**
The following `create-portfolio-share` example shares the specified portfolio with the specified account.

```
aws servicecatalog create-portfolio-share \
    --portfolio-id {{port-2s6abcdef5wdh4}} \
    --account-id {{794123456789}}
```
This command produceds no output.
+  For API details, see [CreatePortfolioShare](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/create-portfolio-share.html) in *AWS CLI Command Reference*.

### `create-portfolio`
<a name="service-catalog_CreatePortfolio_cli_2_topic"></a>

The following code example shows how to use `create-portfolio`.

**AWS CLI**
**To create a portfolio**
The following `create-portfolio` example creates a portfolio.

```
aws servicecatalog create-portfolio  \
    --provider-name {{my-provider}} \
    --display-name {{my-portfolio}}
```
Output:

```
{
    "PortfolioDetail": {
        "ProviderName": "my-provider",
        "DisplayName": "my-portfolio",
        "CreatedTime": 1571337221.555,
        "ARN": "arn:aws:catalog:us-east-2:123456789012:portfolio/port-2s6xmplq5wdh4",
        "Id": "port-2s6xmplq5wdh4"
    }
}
```
+  For API details, see [CreatePortfolio](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/create-portfolio.html) in *AWS CLI Command Reference*.

### `create-product`
<a name="service-catalog_CreateProduct_cli_2_topic"></a>

The following code example shows how to use `create-product`.

**AWS CLI**
**To create a product**
The following `create-product` example creates a product, using a JSON file to pass parameters.

```
aws servicecatalog create-product \
    --cli-input-json {{file://create-product-input.json}}
```
Contents of `create-product-input.json`:

```
{
    "AcceptLanguage": "en",
    "Name": "test-product",
    "Owner": "test-owner",
    "Description": "test-description",
    "Distributor": "test-distributor",
    "SupportDescription": "test-support",
    "SupportEmail": "test@amazon.com",
    "SupportUrl": "https://aws.amazon.com",
    "ProductType": "CLOUD_FORMATION_TEMPLATE",
    "Tags": [
        {
            "Key": "region",
            "Value": "us-east-1"
        }
    ],
    "ProvisioningArtifactParameters": {
        "Name": "test-version-name",
        "Description": "test-version-description",
        "Info": {
            "LoadTemplateFromURL": "https://s3-us-west-1.amazonaws.com/cloudformation-templates-us-west-1/my-cfn-template.template"
        },
        "Type": "CLOUD_FORMATION_TEMPLATE"
    }
}
```
Output:

```
{
    "Tags": [
        {
            "Key": "region",
            "Value": "us-east-1"
        }
    ],
    "ProductViewDetail": {
        "CreatedTime": 1576025036.0,
        "ProductARN": "arn:aws:catalog:us-west-2:1234568542028:product/prod-3p5abcdef3oyk",
        "Status": "CREATED",
        "ProductViewSummary": {
            "Type": "CLOUD_FORMATION_TEMPLATE",
            "Distributor": "test-distributor",
            "SupportUrl": "https://aws.amazon.com",
            "SupportEmail": "test@amazon.com",
            "Id": "prodview-abcd42wvx45um",
            "SupportDescription": "test-support",
            "ShortDescription": "test-description",
            "Owner": "test-owner",
            "Name": "test-product2",
            "HasDefaultPath": false,
            "ProductId": "prod-3p5abcdef3oyk"
        }
    },
    "ProvisioningArtifactDetail": {
        "CreatedTime": 1576025036.0,
        "Active": true,
        "Id": "pa-pq3p5lil12a34",
        "Description": "test-version-description",
        "Name": "test-version-name",
        "Type": "CLOUD_FORMATION_TEMPLATE"
    }
}
```
+  For API details, see [CreateProduct](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/create-product.html) in *AWS CLI Command Reference*.

### `create-provisioned-product-plan`
<a name="service-catalog_CreateProvisionedProductPlan_cli_2_topic"></a>

The following code example shows how to use `create-provisioned-product-plan`.

**AWS CLI**
**To create a plan**
The following `create-provisioned-product-plan` example creates a plan.

```
aws servicecatalog create-provisioned-product-plan \
    --plan-name {{test-plan}} \
    --plan-type {{CLOUDFORMATION}} \
    --product-id {{prod-cfrfxmraxxxxx}} \
    --provisioned-product-name {{test-pp}} \
    --provisioning-artifact-id {{pa-7wz4cu5cxxxxx}}
```
Output:

```
{
    "PlanName": "test-plan",
    "PlanId": "plan-cuxae3z6gxxxx",
    "ProvisionProductId": "pp-7kh7wbc4xxxxx",
    "ProvisionedProductName": "test-pp",
    "ProvisioningArtifactId": "pa-7wz4cu5cxxxxx"
}
```
For more information, see [Creating a launch plan](https://docs.aws.amazon.com/servicecatalog/latest/userguide/launch-plan.html) in the *AWS Service Catalog User Guide*.
+  For API details, see [CreateProvisionedProductPlan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/create-provisioned-product-plan.html) in *AWS CLI Command Reference*.

### `create-provisioning-artifact`
<a name="service-catalog_CreateProvisioningArtifact_cli_2_topic"></a>

The following code example shows how to use `create-provisioning-artifact`.

**AWS CLI**
**To create a provisioning artifact**
The following `create-provisioning-artifact` example creates a provisioning artifact, using a JSON file to pass parameters.

```
aws servicecatalog create-provisioning-artifact \
   --cli-input-json {{file://create-provisioning-artifact-input.json}}
```
Contents of `create-provisioning-artifact-input.json`:

```
{
    "ProductId": "prod-nfi2abcdefghi",
    "Parameters": {
        "Name": "test-provisioning-artifact",
        "Description": "test description",
        "Info": {
            "LoadTemplateFromURL": "https://s3-us-west-1.amazonaws.com/cloudformation-templates-us-west-1/my-cfn-template.template"
        },
        "Type": "CLOUD_FORMATION_TEMPLATE"
    }
}
```
Output:

```
{
    "Info": {
        "TemplateUrl": "https://s3-us-west-1.amazonaws.com/cloudformation-templates-us-west-1/my-cfn-template.template"
    },
    "Status": "CREATING",
    "ProvisioningArtifactDetail": {
        "Id": "pa-bb4abcdefwnaio",
        "Name": "test-provisioning-artifact",
        "Description": "test description",
        "Active": true,
        "Type": "CLOUD_FORMATION_TEMPLATE",
        "CreatedTime": 1576022545.0
    }
}
```
+  For API details, see [CreateProvisioningArtifact](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/create-provisioning-artifact.html) in *AWS CLI Command Reference*.

### `create-tag-option`
<a name="service-catalog_CreateTagOption_cli_2_topic"></a>

The following code example shows how to use `create-tag-option`.

**AWS CLI**
**To create a TagOption**
The following `create-tag-option` example creates a TagOption.

```
aws servicecatalog create-tag-option
    --key {{1234}}
    --value {{name}}
```
Output:

```
{
    "TagOptionDetail": {
    "Id": "tag-iabcdn4fzjjms",
    "Value": "name",
    "Active": true,
    "Key": "1234"
    }
}
```
+  For API details, see [CreateTagOption](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/create-tag-option.html) in *AWS CLI Command Reference*.

### `delete-constraint`
<a name="service-catalog_DeleteConstraint_cli_2_topic"></a>

The following code example shows how to use `delete-constraint`.

**AWS CLI**
**To delete a constraint**
The following `delete-constraint` example deletes a constraint.

```
aws servicecatalog delete-constraint \
    --id {{cons-7tr6gei4bxxxx}}
```
This command produces no output.
For more information, see [Using AWS Service Catalog Constraints](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/constraints.html) in the *AWS Service Catalog User Guide*.
+  For API details, see [DeleteConstraint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/delete-constraint.html) in *AWS CLI Command Reference*.

### `delete-portfolio-share`
<a name="service-catalog_DeletePortfolioShare_cli_2_topic"></a>

The following code example shows how to use `delete-portfolio-share`.

**AWS CLI**
**To stop sharing a portfolio with an account**
The following `delete-portfolio-share` example stops sharing the portfolio with the specified account.

```
aws servicecatalog delete-portfolio-share \
    --portfolio-id {{port-2s6abcdq5wdh4}} \
    --account-id {{123456789012}}
```
This command produces no output.
+  For API details, see [DeletePortfolioShare](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/delete-portfolio-share.html) in *AWS CLI Command Reference*.

### `delete-portfolio`
<a name="service-catalog_DeletePortfolio_cli_2_topic"></a>

The following code example shows how to use `delete-portfolio`.

**AWS CLI**
**To delete a portfolio**
The following `delete-portfolio` example deletes the specified portfolio.

```
aws servicecatalog delete-portfolio \
    --id {{port-abcdlx4gox4do}}
```
This command produces no output.
+  For API details, see [DeletePortfolio](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/delete-portfolio.html) in *AWS CLI Command Reference*.

### `delete-product`
<a name="service-catalog_DeleteProduct_cli_2_topic"></a>

The following code example shows how to use `delete-product`.

**AWS CLI**
**To delete a product**
The following `delete-product` example deletes the specified product.

```
aws servicecatalog delete-product \
    --id {{prod-abcdcek6yhbxi}}
```
This command produces no output.
+  For API details, see [DeleteProduct](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/delete-product.html) in *AWS CLI Command Reference*.

### `delete-provisioned-product-plan`
<a name="service-catalog_DeleteProvisionedProductPlan_cli_2_topic"></a>

The following code example shows how to use `delete-provisioned-product-plan`.

**AWS CLI**
**To delete a provisioned product plan**
The following `delete-provisioned-product-plan` example deletes a provisioned product plan.

```
aws servicecatalog delete-provisioned-product-plan \
    --plan-id {{plan-cuxae3z6gxxxx}}
```
This command produces no output.
For more information, see [Creating a launch plan](https://docs.aws.amazon.com/servicecatalog/latest/userguide/launch-plan.html) in the *AWS Service Catalog User Guide*.
+  For API details, see [DeleteProvisionedProductPlan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/delete-provisioned-product-plan.html) in *AWS CLI Command Reference*.

### `delete-provisioning-artifact`
<a name="service-catalog_DeleteProvisioningArtifact_cli_2_topic"></a>

The following code example shows how to use `delete-provisioning-artifact`.

**AWS CLI**
**To delete a provisioning artifact**
The following `delete-provisioning-artifact` example deletes the specified provisioning artifact.

```
aws servicecatalog delete-provisioning-artifact \
    --product-id {{prod-abc2uebuplcpw}} \
    --provisioning-artifact-id {{pa-pqabcddii7ouc}}
```
This command produces no output.
+  For API details, see [DeleteProvisioningArtifact](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/delete-provisioning-artifact.html) in *AWS CLI Command Reference*.

### `delete-tag-option`
<a name="service-catalog_DeleteTagOption_cli_2_topic"></a>

The following code example shows how to use `delete-tag-option`.

**AWS CLI**
**To delete a TagOption**
The following `delete-tag-option` example deletes the specified TagOption.

```
aws servicecatalog delete-tag-option \
    --id {{tag-iabcdn4fzjjms}}
```
This command produces no output.
+  For API details, see [DeleteTagOption](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/delete-tag-option.html) in *AWS CLI Command Reference*.

### `describe-constraint`
<a name="service-catalog_DescribeConstraint_cli_2_topic"></a>

The following code example shows how to use `describe-constraint`.

**AWS CLI**
**To describe a constraint**
The following `describe-constraint` example describes a constraint.

```
aws servicecatalog describe-constraint \
    --id {{"cons-oqp52evr4bxxxx"}}
```
Output:

```
{
    "ConstraintDetail": {
        "ConstraintId": "cons-7tr6gei4bxxxx",
        "Type": "LAUNCH",
        "Owner": "123456789012",
        "ProductId": "prod-cfrfxmra3xxxx",
        "PortfolioId": "port-y3fnkeslpxxxx"
    },
    "ConstraintParameters": "{\"RoleArn\" : \"arn:aws:iam::123456789012:role/LaunchRole\"}",
    "Status": "AVAILABLE"
}
```
For more information, see [Using AWS Service Catalog Constraints](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/constraints.html) in the *AWS Service Catalog User Guide*.
+  For API details, see [DescribeConstraint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-constraint.html) in *AWS CLI Command Reference*.

### `describe-copy-product-status`
<a name="service-catalog_DescribeCopyProductStatus_cli_2_topic"></a>

The following code example shows how to use `describe-copy-product-status`.

**AWS CLI**
**To describe the status of the copy product operation**
The following `describe-copy-product-status` example displays the current status of the specified asynchronous copy product operation.

```
aws servicecatalog describe-copy-product-status \
    --copy-product-token {{copyproduct-znn5tf5abcd3w}}
```
Output:

```
{
    "CopyProductStatus": "SUCCEEDED",
    "TargetProductId": "prod-os6hog7abcdt2"
}
```
+  For API details, see [DescribeCopyProductStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-copy-product-status.html) in *AWS CLI Command Reference*.

### `describe-portfolio-share-status`
<a name="service-catalog_DescribePortfolioShareStatus_cli_2_topic"></a>

The following code example shows how to use `describe-portfolio-share-status`.

**AWS CLI**
**To describe portfolio share status**
The following `describe-portfolio-share-status` example describes portfolio share status.

```
aws servicecatalog describe-portfolio-share-status \
    --portfolio-share-token {{"share-agngcybu4xxxx"}}
```
Output:

```
{
    "PortfolioShareToken": "share-agngcybu4xxxx",
    "PortfolioId": "port-y3fnkeslxxxxx",
    "OrganizationNodeValue": "123456789012",
    "Status": "COMPLETED",
    "ShareDetails": {
        "SuccessfulShares": [
            "012345678901"
        ],
        "ShareErrors": []
    }
}
```
For more information, see [Sharing a Portfolio](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs_portfolios_sharing_how-to-share.html) in the *AWS Service Catalog User Guide*.
+  For API details, see [DescribePortfolioShareStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-portfolio-share-status.html) in *AWS CLI Command Reference*.

### `describe-portfolio-shares`
<a name="service-catalog_DescribePortfolioShares_cli_2_topic"></a>

The following code example shows how to use `describe-portfolio-shares`.

**AWS CLI**
**To describe portfolio shares**
The following `describe-portfolio-shares` example describes portfolio shares.

```
aws servicecatalog describe-portfolio-shares \
    --portfolio-id {{port-y3fnkeslxxxxx}} \
    --type {{ACCOUNT}}
```
Output:

```
{
    "PortfolioShareDetails": [
        {
            "PrincipalId": "123456789012",
            "Type": "ACCOUNT",
            "Accepted": true,
            "ShareTagOptions": false,
            "SharePrincipals": false
        },
        {
            "PrincipalId": "123456789012",
            "Type": "ACCOUNT",
            "Accepted": false,
            "ShareTagOptions": false,
            "SharePrincipals": false
        }
    ]
}
```
For more information, see [Sharing a Portfolio](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs_portfolios_sharing_how-to-share.html) in the *AWS Service Catalog User Guide*.
+  For API details, see [DescribePortfolioShares](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-portfolio-shares.html) in *AWS CLI Command Reference*.

### `describe-portfolio`
<a name="service-catalog_DescribePortfolio_cli_2_topic"></a>

The following code example shows how to use `describe-portfolio`.

**AWS CLI**
**To describe a portfolio**
The following `describe-portfolio` example displays details for the specified portfolio.

```
aws servicecatalog describe-portfolio \
    --id {{port-2s6abcdq5wdh4}}
```
Output:

```
{
    "TagOptions": [],
    "PortfolioDetail": {
        "ARN": "arn:aws:catalog:us-west-2:687558541234:portfolio/port-2s6abcdq5wdh4",
        "Id": "port-2s6wuzyq5wdh4",
        "CreatedTime": 1571337221.555,
        "DisplayName": "my-portfolio",
        "ProviderName": "my-provider"
    },
    "Tags": []
}
```
+  For API details, see [DescribePortfolio](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-portfolio.html) in *AWS CLI Command Reference*.

### `describe-product-as-admin`
<a name="service-catalog_DescribeProductAsAdmin_cli_2_topic"></a>

The following code example shows how to use `describe-product-as-admin`.

**AWS CLI**
**To describe a product as an administrator**
The following `describe-product-as-admin` example displays details for the specified product using administrator privileges.

```
aws servicecatalog describe-product-as-admin \
    --id {{prod-abcdcek6yhbxi}}
```
Output:

```
{
    "TagOptions": [],
    "ProductViewDetail": {
        "ProductARN": "arn:aws:catalog:us-west-2:687558542028:product/prod-abcdcek6yhbxi",
        "ProductViewSummary": {
            "SupportEmail": "test@amazon.com",
            "Type": "CLOUD_FORMATION_TEMPLATE",
            "Distributor": "test-distributor",
            "ShortDescription": "test-description",
            "Owner": "test-owner",
            "Id": "prodview-wi3l2j4abc6vc",
            "SupportDescription": "test-support",
            "ProductId": "prod-abcdcek6yhbxi",
            "HasDefaultPath": false,
            "Name": "test-product3",
            "SupportUrl": "https://aws.amazon.com"
        },
        "CreatedTime": 1577136715.0,
        "Status": "CREATED"
    },
    "ProvisioningArtifactSummaries": [
        {
            "CreatedTime": 1577136715.0,
            "Description": "test-version-description",
            "ProvisioningArtifactMetadata": {
                "SourceProvisioningArtifactId": "pa-abcdxkkiv5fcm"
            },
            "Name": "test-version-name-3",
            "Id": "pa-abcdxkkiv5fcm"
        }
    ],
    "Tags": [
        {
            "Value": "iad",
            "Key": "region"
        }
    ]
}
```
+  For API details, see [DescribeProductAsAdmin](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-product-as-admin.html) in *AWS CLI Command Reference*.

### `describe-product`
<a name="service-catalog_DescribeProduct_cli_2_topic"></a>

The following code example shows how to use `describe-product`.

**AWS CLI**
**To describe a product**
The following `describe-product` example describes a product.

```
aws servicecatalog describe-product \
    --id {{prod-dybl43puxxxxx}}
```
Output:

```
{
    "ProductViewSummary": {
        "Id": "prodview-vkvy2kum5xxxx",
        "ProductId": "prod-dybl43puxxxxx",
        "Name": "ec2-test",
        "Owner": "user",
        "ShortDescription": "",
        "Type": "CLOUD_FORMATION_TEMPLATE",
        "Distributor": "",
        "HasDefaultPath": false,
        "SupportEmail": "",
        "SupportDescription": "",
        "SupportUrl": ""
    },
    "ProvisioningArtifacts": [
        {
            "Id": "pa-j7fs6ybztxxxx",
            "Name": "v2",
            "Description": "",
            "CreatedTime": "2021-07-16T15:20:24-05:00",
            "Guidance": "DEFAULT"
        },
        {
            "Id": "pa-s6z7i2nivxxxx",
            "Description": "Create EC2 and KMS",
            "CreatedTime": "2024-06-13T18:27:54-05:00",
            "Guidance": "DEFAULT"
        },
        {
            "Id": "pa-6573v3bloxxxx",
            "Name": "v3",
            "CreatedTime": "2024-06-13T18:45:14-05:00",
            "Guidance": "DEFAULT"
        }
    ],
    "Budgets": [],
    "LaunchPaths": [
        {
            "Id": "lpv3-y3fnkeslpxxxx",
            "Name": "TestPort"
        }
    ]
}
```
For more information, see [Managing Products](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs_products.html) in the *AWS Service Catalog User Guide*.
+  For API details, see [DescribeProduct](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-product.html) in *AWS CLI Command Reference*.

### `describe-provisioned-product-plan`
<a name="service-catalog_DescribeProvisionedProductPlan_cli_2_topic"></a>

The following code example shows how to use `describe-provisioned-product-plan`.

**AWS CLI**
**To describe a provisioned product plan**
The following `describe-provisioned-product-plan` example describes a provisioned product plan.

```
aws servicecatalog describe-provisioned-product-plan \
    --plan-id {{"plan-g7iwsaf3mxxxx"}}
```
Output:

```
{
    "ProvisionedProductPlanDetails": {
        "CreatedTime": "2025-11-09T18:09:37.808000-06:00",
        "PathId": "lpv3-y3fnkeslpxxxx",
        "ProductId": "prod-cfrfxmraxxxxx",
        "PlanName": "test-plan",
        "PlanId": "plan-g7iwsaf3mxxxx",
        "ProvisionProductId": "pp-mkbnbztzxxxxx",
        "ProvisionProductName": "test-pp",
        "PlanType": "CLOUDFORMATION",
        "ProvisioningArtifactId": "pa-7wz4cu5cxxxxx",
        "Status": "CREATE_SUCCESS",
        "UpdatedTime": "2025-11-09T18:09:46.524000-06:00",
        "Tags": []
    }
}
```
For more information, see [Creating a launch plan](https://docs.aws.amazon.com/servicecatalog/latest/userguide/launch-plan.html) in the *AWS Service Catalog User Guide*.
+  For API details, see [DescribeProvisionedProductPlan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-provisioned-product-plan.html) in *AWS CLI Command Reference*.

### `describe-provisioned-product`
<a name="service-catalog_DescribeProvisionedProduct_cli_2_topic"></a>

The following code example shows how to use `describe-provisioned-product`.

**AWS CLI**
**To describe a provisioned product**
The following `describe-provisioned-product` example displays details for the specified provisioned product.

```
aws servicecatalog describe-provisioned-product \
    --id {{pp-dpom27bm4abcd}}
```
Output:

```
{
    "ProvisionedProductDetail": {
        "Status": "ERROR",
        "CreatedTime": 1577222793.358,
        "Arn": "arn:aws:servicecatalog:us-west-2:123456789012:stack/mytestppname3/pp-dpom27bm4abcd",
        "Id": "pp-dpom27bm4abcd",
        "StatusMessage": "AmazonCloudFormationException  Parameters: [KeyName] must have values (Service: AmazonCloudFormation; Status Code: 400; Error Code: ValidationError; Request ID: 5528602a-a9ef-427c-825c-f82c31b814f5)",
        "IdempotencyToken": "527c5358-2a1a-4b9e-b1b9-7293b0ddff42",
        "LastRecordId": "rec-tfuawdjovzxge",
        "Type": "CFN_STACK",
        "Name": "mytestppname3"
    },
    "CloudWatchDashboards": []
}
```
+  For API details, see [DescribeProvisionedProduct](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-provisioned-product.html) in *AWS CLI Command Reference*.

### `describe-provisioning-artifact`
<a name="service-catalog_DescribeProvisioningArtifact_cli_2_topic"></a>

The following code example shows how to use `describe-provisioning-artifact`.

**AWS CLI**
**To describe a provisioning artifact**
The following `describe-provisioning-artifact` example displays details for the specified provisioning artifact.

```
aws servicecatalog describe-provisioning-artifact \
    --provisioning-artifact-id {{pa-pcz347abcdcfm}} \
    --product-id {{prod-abcdfz3syn2rg}}
```
Output:

```
{
    "Info": {
        "TemplateUrl": "https://awsdocs.s3.amazonaws.com/servicecatalog/myexampledevelopment-environment.template"
    },
    "ProvisioningArtifactDetail": {
        "Id": "pa-pcz347abcdcfm",
        "Active": true,
        "Type": "CLOUD_FORMATION_TEMPLATE",
        "Description": "updated description",
        "CreatedTime": 1562097906.0,
        "Name": "updated name"
    },
    "Status": "AVAILABLE"
}
```
+  For API details, see [DescribeProvisioningArtifact](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-provisioning-artifact.html) in *AWS CLI Command Reference*.

### `describe-provisioning-parameters`
<a name="service-catalog_DescribeProvisioningParameters_cli_2_topic"></a>

The following code example shows how to use `describe-provisioning-parameters`.

**AWS CLI**
**To describe provisioning parameters**
The following `describe-provisioning-parameters` example describes provisioning parameters.

```
aws servicecatalog describe-provisioning-parameters \
    --product-id {{prod-cfrfxmraxxxxx}} \
    --provisioning-artifact-id {{pa-7wz4cu5cxxxxx}} \
    --path-id {{lpv3-y3fnkeslpxxxx}}
```
Output:

```
{
    "ProvisioningArtifactParameters": [
        {
            "ParameterKey": "Size",
            "ParameterType": "String",
            "IsNoEcho": false,
            "ParameterConstraints": {
                "AllowedValues": []
            }
        }
    ],
    "ConstraintSummaries": [
        {
            "Type": "LAUNCH"
        }
    ],
    "UsageInstructions": [
        {
            "Type": "rules",
            "Value": "{}"
        },
        {
            "Type": "version",
            "Value": "2010-09-09"
        },
        {
            "Type": "launchAsRole",
            "Value": "arn:aws:iam::123456789012:role/NewLaunchRole"
        },
        {
            "Type": "tagUpdateOnProvisionedProduct",
            "Value": "NOT_ALLOWED"
        }
    ],
    "TagOptions": [
        {
            "Key": "Application Name",
            "Values": [
                "Testing Tag",
                "Testing Tag Options"
            ]
        }
    ],
    "ProvisioningArtifactPreferences": {},
    "ProvisioningArtifactOutputs": [
        {
            "Key": "pa-7wz4cu5cxxxxx",
            "Description": ""
        }
    ],
    "ProvisioningArtifactOutputKeys": []
}
```
For more information, see [Launching a product](https://docs.aws.amazon.com/servicecatalog/latest/userguide/enduser-launch.html) in the *AWS Service Catalog User Guide*.
+  For API details, see [DescribeProvisioningParameters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-provisioning-parameters.html) in *AWS CLI Command Reference*.

### `describe-tag-option`
<a name="service-catalog_DescribeTagOption_cli_2_topic"></a>

The following code example shows how to use `describe-tag-option`.

**AWS CLI**
**To describe a TagOption**
The following `describe-tag-option` example displays details for the specified TagOption.

```
aws servicecatalog describe-tag-option \
    --id {{tag-p3tej2abcd5qc}}
```
Output:

```
{
    "TagOptionDetail": {
        "Active": true,
        "Id": "tag-p3tej2abcd5qc",
        "Value": "value-3",
        "Key": "1234"
    }
}
```
+  For API details, see [DescribeTagOption](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/describe-tag-option.html) in *AWS CLI Command Reference*.

### `disassociate-principal-from-portfolio`
<a name="service-catalog_DisassociatePrincipalFromPortfolio_cli_2_topic"></a>

The following code example shows how to use `disassociate-principal-from-portfolio`.

**AWS CLI**
**To disassociate a principal from a portfolio**
The following `disassociate-principal-from-portfolio` example disassociates the specified principal from the portfolio.

```
aws servicecatalog disassociate-principal-from-portfolio \
    --portfolio-id {{port-2s6abcdq5wdh4}} \
    --principal-arn {{arn:aws:iam::123456789012:group/myendusers}}
```
This command produces no output.
+  For API details, see [DisassociatePrincipalFromPortfolio](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/disassociate-principal-from-portfolio.html) in *AWS CLI Command Reference*.

### `disassociate-product-from-portfolio`
<a name="service-catalog_DisassociateProductFromPortfolio_cli_2_topic"></a>

The following code example shows how to use `disassociate-product-from-portfolio`.

**AWS CLI**
**To disassociate a product from a portfolio**
The following `disassociate-product-from-portfolio` example disassociates the specified product from the portfolio.

```
aws servicecatalog disassociate-product-from-portfolio \
    --product-id {{prod-3p5abcdmu3oyk}} \
    --portfolio-id {{port-2s6abcdq5wdh4}}
```
This command produces no output.
+  For API details, see [DisassociateProductFromPortfolio](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/disassociate-product-from-portfolio.html) in *AWS CLI Command Reference*.

### `disassociate-tag-option-from-resource`
<a name="service-catalog_DisassociateTagOptionFromResource_cli_2_topic"></a>

The following code example shows how to use `disassociate-tag-option-from-resource`.

**AWS CLI**
**To disassociate a TagOption from a resource**
The following `disassociate-tag-option-from-resource` example disassociates the specified `TagOption` from the resource.

```
aws servicecatalog disassociate-tag-option-from-resource \
     --resource-id {{port-2s6abcdq5wdh4}} \
     --tag-option-id {{tag-p3abc2pkpz5qc}}
```
This command produces no output.
+  For API details, see [DisassociateTagOptionFromResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/disassociate-tag-option-from-resource.html) in *AWS CLI Command Reference*.

### `list-accepted-portfolio-shares`
<a name="service-catalog_ListAcceptedPortfolioShares_cli_2_topic"></a>

The following code example shows how to use `list-accepted-portfolio-shares`.

**AWS CLI**
**To list accepted portfolio shares**
The following `list-accepted-portfolio-shares` example lists all portfolios for which sharing was accepted by this account, including only the default Service Catalog portfolios.

```
aws servicecatalog list-accepted-portfolio-shares \
    --portfolio-share-type {{"AWS_SERVICECATALOG"}}
```
Output:

```
{
    "PortfolioDetails": [
        {
            "ARN": "arn:aws:catalog:us-west-2:123456789012:portfolio/port-d2abcd5dpkuma",
            "Description": "AWS Service Catalog Reference blueprints for often-used AWS services such as EC2, S3, RDS, VPC and EMR.",
            "CreatedTime": 1574456190.687,
            "ProviderName": "AWS Service Catalog",
            "DisplayName": "Reference Architectures",
            "Id": "port-d2abcd5dpkuma"
        },
        {
            "ARN": "arn:aws:catalog:us-west-2:123456789012:portfolio/port-abcdefaua7zpu",
            "Description": "AWS well-architected blueprints for high reliability applications.",
            "CreatedTime": 1574461496.092,
            "ProviderName": "AWS Service Catalog",
            "DisplayName": "High Reliability Architectures",
            "Id": "port-abcdefaua7zpu"
        }
    ]
}
```
+  For API details, see [ListAcceptedPortfolioShares](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/list-accepted-portfolio-shares.html) in *AWS CLI Command Reference*.

### `list-constraints-for-portfolio`
<a name="service-catalog_ListConstraintsForPortfolio_cli_2_topic"></a>

The following code example shows how to use `list-constraints-for-portfolio`.

**AWS CLI**
**Example 1: To list all constraints for a portfolio**
The following `list-constraints-for-portfolio` example lists all constraints for a portfolio.

```
aws servicecatalog list-constraints-for-portfolio \
    --portfolio-id {{port-y3fnkeslpxxxx}}
```
Output:

```
{
    "ConstraintDetails": [
        {
            "ConstraintId": "cons-dgdyqdqrxxxxx",
            "Type": "LAUNCH",
            "Description": "Launch as local role TestLaunchRole",
            "Owner": "123456789012",
            "ProductId": "prod-j6pd3hf6xxxxx",
            "PortfolioId": "port-y3fnkeslxxxxx"
        },
        {
            "ConstraintId": "cons-tzxjnj4l6xxxx",
            "Type": "RESOURCE_UPDATE",
            "Owner": "123456789012",
            "ProductId": "prod-sphewkokxxxxx",
            "PortfolioId": "port-y3fnkeslxxxxx"
        }
    ]
}
```
**Example 2: To list constraints on a product**
The following `list-constraints-for-portfolio` example lists constraints on a product.

```
aws servicecatalog list-constraints-for-portfolio \
    --portfolio-id {{port-y3fnkeslxxxxx}} \
    --product-id {{prod-j6pd3hf6xxxxx}}
```
Output:

```
{
    "ConstraintDetails": [
        {
            "ConstraintId": "cons-dgdyqdqrxxxxx",
            "Type": "LAUNCH",
            "Description": "Launch as local role TestLaunchRole",
            "Owner": "123456789012",
            "ProductId": "prod-j6pd3hf6xxxxx",
            "PortfolioId": "port-y3fnkeslxxxxx"
        }
    ]
}
```
For more information, see [Using AWS Service Catalog Constraints](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/constraints.html) in the *AWS Service Catalog User Guide*.
+  For API details, see [ListConstraintsForPortfolio](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/list-constraints-for-portfolio.html) in *AWS CLI Command Reference*.

### `list-launch-paths`
<a name="service-catalog_ListLaunchPaths_cli_2_topic"></a>

The following code example shows how to use `list-launch-paths`.

**AWS CLI**
**To list launch paths**
The following `list-launch-paths` example lists launch paths for a portfolio.

```
aws servicecatalog list-launch-paths \
    --product-id {{prod-cfrfxmraxxxxx}}
```
Output:

```
{
    "LaunchPathSummaries": [
        {
            "Id": "lpv3-y3fnkeslpxxxx",
            "ConstraintSummaries": [
                {
                    "Type": "LAUNCH"
                }
            ],
            "Tags": [],
            "Name": "TestPort"
        }
    ]
}
```
For more information, see [Granting Access to Users](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs_portfolios_users.html) in the *AWS Service Catalog User Guide*.
+  For API details, see [ListLaunchPaths](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/list-launch-paths.html) in *AWS CLI Command Reference*.

### `list-portfolio-access`
<a name="service-catalog_ListPortfolioAccess_cli_2_topic"></a>

The following code example shows how to use `list-portfolio-access`.

**AWS CLI**
**To list accounts with access to a portfolio**
The following `list-portfolio-access` example lists the AWS accounts that have access to the specified portfolio.

```
aws servicecatalog list-portfolio-access \
    --portfolio-id {{port-2s6abcdq5wdh4}}
```
Output:

```
{
    "AccountIds": [
        "123456789012"
    ]
}
```
+  For API details, see [ListPortfolioAccess](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/list-portfolio-access.html) in *AWS CLI Command Reference*.

### `list-portfolios-for-product`
<a name="service-catalog_ListPortfoliosForProduct_cli_2_topic"></a>

The following code example shows how to use `list-portfolios-for-product`.

**AWS CLI**
**To list portfolios associated with a product**
The following `list-portfolios-for-product` example lists the portfolios associated with the specified product.

```
aws servicecatalog list-portfolios-for-product \
    --product-id {{prod-abcdfz3syn2rg}}
```
Output:

```
{
    "PortfolioDetails": [
        {
            "CreatedTime": 1571337221.555,
            "Id": "port-2s6abcdq5wdh4",
            "ARN": "arn:aws:catalog:us-west-2:123456789012:portfolio/port-2s6abcdq5wdh4",
            "DisplayName": "my-portfolio",
            "ProviderName": "my-provider"
        },
        {
            "CreatedTime": 1559665256.348,
            "Id": "port-5abcd3e5st4ei",
            "ARN": "arn:aws:catalog:us-west-2:123456789012:portfolio/port-5abcd3e5st4ei",
            "DisplayName": "test",
            "ProviderName": "provider-name"
        }
    ]
}
```
+  For API details, see [ListPortfoliosForProduct](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/list-portfolios-for-product.html) in *AWS CLI Command Reference*.

### `list-portfolios`
<a name="service-catalog_ListPortfolios_cli_2_topic"></a>

The following code example shows how to use `list-portfolios`.

**AWS CLI**
**To list portfolios**
The following `list-portfolios` example lists the Service Catalog portfolios in the current Region.

```
aws servicecatalog list-portfolios
```
Output:

```
{
    "PortfolioDetails": [
        {
           "CreatedTime": 1559665256.348,
           "ARN": "arn:aws:catalog:us-east-2:123456789012:portfolio/port-5pzcxmplst4ei",
           "DisplayName": "my-portfolio",
           "Id": "port-5pzcxmplst4ei",
           "ProviderName": "my-user"
        }
    ]
}
```
+  For API details, see [ListPortfolios](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/list-portfolios.html) in *AWS CLI Command Reference*.

### `list-principals-for-portfolio`
<a name="service-catalog_ListPrincipalsForPortfolio_cli_2_topic"></a>

The following code example shows how to use `list-principals-for-portfolio`.

**AWS CLI**
**To list all principals for a portfolio**
The following `list-principals-for-portfolio` example lists all principals for the specified portfolio.

```
aws servicecatalog list-principals-for-portfolio \
    --portfolio-id {{port-2s6abcdq5wdh4}}
```
Output:

```
{
    "Principals": [
        {
            "PrincipalARN": "arn:aws:iam::123456789012:user/usertest",
            "PrincipalType": "IAM"
        }
    ]
}
```
+  For API details, see [ListPrincipalsForPortfolio](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/list-principals-for-portfolio.html) in *AWS CLI Command Reference*.

### `list-provisioning-artifacts`
<a name="service-catalog_ListProvisioningArtifacts_cli_2_topic"></a>

The following code example shows how to use `list-provisioning-artifacts`.

**AWS CLI**
**To list all provisioning artifacts for a product**
The following `list-provisioning-artifacts` example lists all provisioning artifacts for the specified product.

```
aws servicecatalog list-provisioning-artifacts \
    --product-id {{prod-nfi2abcdefgcpw}}
```
Output:

```
{
    "ProvisioningArtifactDetails": [
        {
            "Id": "pa-abcdef54ipm6z",
            "Description": "test-version-description",
            "Type": "CLOUD_FORMATION_TEMPLATE",
            "CreatedTime": 1576021147.0,
            "Active": true,
            "Name": "test-version-name"
        },
        {
            "Id": "pa-bb4zyxwwnaio",
            "Description": "test description",
            "Type": "CLOUD_FORMATION_TEMPLATE",
            "CreatedTime": 1576022545.0,
            "Active": true,
            "Name": "test-provisioning-artifact-2"
        }
    ]
}
```
+  For API details, see [ListProvisioningArtifacts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/list-provisioning-artifacts.html) in *AWS CLI Command Reference*.

### `list-resources-for-tag-option`
<a name="service-catalog_ListResourcesForTagOption_cli_2_topic"></a>

The following code example shows how to use `list-resources-for-tag-option`.

**AWS CLI**
**To list resources associated to a TagOption**
The following `list-resources-for-tag-option` example lists the resources associated with the specified `TagOption`.

```
aws servicecatalog list-resources-for-tag-option \
    --tag-option-id {{tag-p3tej2abcd5qc}}
```
Output:

```
{
    "ResourceDetails": [
        {
            "ARN": "arn:aws:catalog:us-west-2:123456789012:product/prod-abcdfz3syn2rg",
            "Name": "my product",
            "Description": "description",
            "CreatedTime": 1562097906.0,
            "Id": "prod-abcdfz3syn2rg"
        }
    ]
}
```
+  For API details, see [ListResourcesForTagOption](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/list-resources-for-tag-option.html) in *AWS CLI Command Reference*.

### `list-tag-options`
<a name="service-catalog_ListTagOptions_cli_2_topic"></a>

The following code example shows how to use `list-tag-options`.

**AWS CLI**
The following `list-tag-options` example lists all values for `TagOptions`.

```
aws servicecatalog list-tag-options
```
Output:

```
{
    "TagOptionDetails": [
        {
            "Value": "newvalue",
            "Active": true,
            "Id": "tag-iabcdn4fzjjms",
            "Key": "1234"
        },
        {
            "Value": "value1",
            "Active": true,
            "Id": "tag-e3abcdvmwvrzy",
            "Key": "key"
        }
    ]
}
```
+  For API details, see [ListTagOptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/list-tag-options.html) in *AWS CLI Command Reference*.

### `provision-product`
<a name="service-catalog_ProvisionProduct_cli_2_topic"></a>

The following code example shows how to use `provision-product`.

**AWS CLI**
**To provision a product**
The following `provision-product` example provisions the specified product using the specified provisioning artifact.

```
aws servicecatalog provision-product \
    --product-id {{prod-abcdfz3syn2rg}} \
    --provisioning-artifact-id {{pa-abc347pcsccfm}} \
    --provisioned-product-name {{"mytestppname3"}}
```
Output:

```
{
    "RecordDetail": {
        "RecordId": "rec-tfuawdabcdege",
        "CreatedTime": 1577222793.362,
        "ProvisionedProductId": "pp-abcd27bm4mldq",
        "PathId": "lpv2-abcdg3jp6t5k6",
        "RecordErrors": [],
        "ProductId": "prod-abcdfz3syn2rg",
        "UpdatedTime": 1577222793.362,
        "RecordType": "PROVISION_PRODUCT",
        "ProvisionedProductName": "mytestppname3",
        "ProvisioningArtifactId": "pa-pcz347abcdcfm",
        "RecordTags": [],
        "Status": "CREATED",
        "ProvisionedProductType": "CFN_STACK"
    }
}
```
+  For API details, see [ProvisionProduct](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/provision-product.html) in *AWS CLI Command Reference*.

### `reject-portfolio-share`
<a name="service-catalog_RejectPortfolioShare_cli_2_topic"></a>

The following code example shows how to use `reject-portfolio-share`.

**AWS CLI**
**To reject a portfolio share**
The following `reject-portfolio-share` example rejects the portfolio share for the given portfolio.

```
aws servicecatalog reject-portfolio-share \
    --portfolio-id {{port-2s6wuabcdefghijk}}
```
This command produces no output.
+  For API details, see [RejectPortfolioShare](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/reject-portfolio-share.html) in *AWS CLI Command Reference*.

### `scan-provisioned-products`
<a name="service-catalog_ScanProvisionedProducts_cli_2_topic"></a>

The following code example shows how to use `scan-provisioned-products`.

**AWS CLI**
**To list all available provisioned products**
The following `scan-provisioned-products` example lists available provisioned products.

```
aws servicecatalog scan-provisioned-products
```
Output:

```
{
    "ProvisionedProducts": [
        {
            "Status": "ERROR",
            "Arn": "arn:aws:servicecatalog:us-west-2:123456789012:stack/mytestppname3/pp-abcd27bm4mldq",
            "StatusMessage": "AmazonCloudFormationException  Parameters: [KeyName] must have values (Service: AmazonCloudFormation; Status Code: 400; Error Code: ValidationError; Request ID: 5528602a-a9ef-427c-825c-f82c31b814f5)",
            "Id": "pp-abcd27bm4mldq",
            "Type": "CFN_STACK",
            "IdempotencyToken": "527c5358-2a1a-4b9e-b1b9-7293b0ddff42",
            "CreatedTime": 1577222793.358,
            "Name": "mytestppname3",
            "LastRecordId": "rec-tfuawdabcdxge"
        }
    ]
}
```
+  For API details, see [ScanProvisionedProducts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/scan-provisioned-products.html) in *AWS CLI Command Reference*.

### `search-products-as-admin`
<a name="service-catalog_SearchProductsAsAdmin_cli_2_topic"></a>

The following code example shows how to use `search-products-as-admin`.

**AWS CLI**
**To search products with administrator privileges**
The following `search-products-as-admin` example searches for products with admin privileges, using a portfolio ID as a filter.

```
aws servicecatalog search-products-as-admin \
    --portfolio-id {{port-5abcd3e5st4ei}}
```
Output:

```
{
    "ProductViewDetails": [
        {
            "ProductViewSummary": {
                "Name": "my product",
                "Owner": "owner name",
                "Type": "CLOUD_FORMATION_TEMPLATE",
                "ProductId": "prod-abcdfz3syn2rg",
                "HasDefaultPath": false,
                "Id": "prodview-abcdmyuzv2dlu",
                "ShortDescription": "description"
            },
            "ProductARN": "arn:aws:catalog:us-west-2:123456789012:product/prod-abcdfz3syn2rg",
            "CreatedTime": 1562097906.0,
            "Status": "CREATED"
        }
    ]
}
```
+  For API details, see [SearchProductsAsAdmin](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/search-products-as-admin.html) in *AWS CLI Command Reference*.

### `search-products`
<a name="service-catalog_SearchProducts_cli_2_topic"></a>

The following code example shows how to use `search-products`.

**AWS CLI**
**To get information about the products to which the caller has access**
The following `search-products` example gets all the products the caller has access to.

```
aws servicecatalog search-products
```
Output:

```
{
    "ProductViewSummaries": [
        {
            "Id": "prodview-5uksdh4xxxxxx",
            "ProductId": "prod-j6fu3hxxxxxxxx",
            "Name": "TestSC",
            "Owner": "test",
            "ShortDescription": "",
            "Type": "CLOUD_FORMATION_TEMPLATE",
            "Distributor": "",
            "HasDefaultPath": false,
            "SupportEmail": "",
            "SupportDescription": "",
            "SupportUrl": ""
        },
        {
            "Id": "prodview-3kfoaabxxxxxx",
            "ProductId": "prod-j6pd3xxxxxxxx",
            "Name": "TestProduct",
            "Owner": "test_owner",
            "ShortDescription": "",
            "Type": "CLOUD_FORMATION_TEMPLATE",
            "Distributor": "",
            "HasDefaultPath": false,
            "SupportEmail": "",
            "SupportDescription": "",
            "SupportUrl": ""
        }
    ]
}
```
For more information, see [Managing Products](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs_products.html) in the *AWS Service Catalog User Guide*.
+  For API details, see [SearchProducts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/search-products.html) in *AWS CLI Command Reference*.

### `search-provisioned-products`
<a name="service-catalog_SearchProvisionedProducts_cli_2_topic"></a>

The following code example shows how to use `search-provisioned-products`.

**AWS CLI**
**To search provisioned products**
The following `search-provisioned-products` example searches for provisioned products matching the specified product ID, using a JSON file to pass parameters.

```
aws servicecatalog search-provisioned-products \
    --cli-input-json {{file://search-provisioned-products-input.json}}
```
Contents of `search-provisioned-products-input.json`:

```
{
    "Filters": {
        "SearchQuery": [
            "prod-tcjvfz3syn2rg"
        ]
    }
}
```
Output:

```
{
    "ProvisionedProducts": [
        {
            "ProvisioningArtifactId": "pa-pcz347abcdcfm",
            "Name": "mytestppname3",
            "CreatedTime": 1577222793.358,
            "Id": "pp-abcd27bm4mldq",
            "Status": "ERROR",
            "UserArn": "arn:aws:iam::123456789012:user/cliuser",
            "StatusMessage": "AmazonCloudFormationException  Parameters: [KeyName] must have values (Service: AmazonCloudFormation; Status Code: 400; Error Code: ValidationError; Request ID: 5528602a-a9ef-427c-825c-f82c31b814f5)",
            "Arn": "arn:aws:servicecatalog:us-west-2:123456789012:stack/mytestppname3/pp-abcd27bm4mldq",
            "Tags": [
                {
                    "Value": "arn:aws:catalog:us-west-2:123456789012:product/prod-abcdfz3syn2rg",
                    "Key": "aws:servicecatalog:productArn"
                },
                {
                    "Value": "arn:aws:iam::123456789012:user/cliuser",
                    "Key": "aws:servicecatalog:provisioningPrincipalArn"
                },
                {
                    "Value": "value-3",
                    "Key": "1234"
                },
                {
                    "Value": "pa-pcz347abcdcfm",
                    "Key": "aws:servicecatalog:provisioningArtifactIdentifier"
                },
                {
                    "Value": "arn:aws:catalog:us-west-2:123456789012:portfolio/port-2s6abcdq5wdh4",
                    "Key": "aws:servicecatalog:portfolioArn"
                },
                {
                    "Value": "arn:aws:servicecatalog:us-west-2:123456789012:stack/mytestppname3/pp-abcd27bm4mldq",
                    "Key": "aws:servicecatalog:provisionedProductArn"
                }
            ],
            "IdempotencyToken": "527c5358-2a1a-4b9e-b1b9-7293b0ddff42",
            "UserArnSession": "arn:aws:iam::123456789012:user/cliuser",
            "Type": "CFN_STACK",
            "LastRecordId": "rec-tfuawdabcdxge",
            "ProductId": "prod-abcdfz3syn2rg"
        }
    ],
    "TotalResultsCount": 1
}
```
+  For API details, see [SearchProvisionedProducts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/search-provisioned-products.html) in *AWS CLI Command Reference*.

### `terminate-provisioned-product`
<a name="service-catalog_TerminateProvisionedProduct_cli_2_topic"></a>

The following code example shows how to use `terminate-provisioned-product`.

**AWS CLI**
**To terminate a provisioned product**
The following `terminate-provisioned-product` example terminates a provisioned product.

```
aws servicecatalog terminate-provisioned-product \
    --provisioned-product-id {{pp-7z4t3k4hxxxxx}}
```
Output:

```
{
    "RecordDetail": {
        "RecordId": "rec-sbwnhzld3xxxx",
        "ProvisionedProductName": "test2",
        "Status": "CREATED",
        "CreatedTime": "2025-12-31T15:23:55.051000-06:00",
        "UpdatedTime": "2025-12-31T15:23:55.051000-06:00",
        "ProvisionedProductType": "CFN_STACK",
        "RecordType": "TERMINATE_PROVISIONED_PRODUCT",
        "ProvisionedProductId": "pp-7z4t3k4hxxxxx",
        "ProductId": "prod-j6pd3hf6xxxxx",
        "ProvisioningArtifactId": "pa-sbhovlh7wxxxx",
        "PathId": "lpv3-y3fnkeslpxxxx",
        "RecordErrors": [],
        "RecordTags": [],
        "LaunchRoleArn": "arn:aws:iam::123456789012:role/TestLaunchRole"
    }
}
```
For more information, see [Managing Provisioned Products](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/provisioned-products.html) in the *AWS Service Catalog User Guide*.
+  For API details, see [TerminateProvisionedProduct](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/terminate-provisioned-product.html) in *AWS CLI Command Reference*.

### `update-constraint`
<a name="service-catalog_UpdateConstraint_cli_2_topic"></a>

The following code example shows how to use `update-constraint`.

**AWS CLI**
**To update a constraint**
The following `update-constraint` example updates a constraint.

```
aws servicecatalog update-constraint \
    --id {{cons-dgdyqdqrxxxxx}} \
    --parameters '{{{"LocalRoleName": "TestLaunchRole"}}}'
```
Output:

```
{
    "ConstraintDetail": {
        "ConstraintId": "cons-dgdyqdqrxxxxx",
        "Type": "LAUNCH",
        "Description": "Launch as local role TestLaunchRole",
        "Owner": "123456789012",
        "ProductId": "prod-j6pd3hf6xxxxx",
        "PortfolioId": "port-y3fnkeslxxxxx"
    },
    "ConstraintParameters": "{\"LocalRoleName\": \"TestLaunchRole\"}",
    "Status": "CREATING"
}
```
For more information, see [Using AWS Service Catalog Constraints](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/constraints.html) in the *AWS Service Catalog User Guide*.
+  For API details, see [UpdateConstraint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/update-constraint.html) in *AWS CLI Command Reference*.

### `update-portfolio`
<a name="service-catalog_UpdatePortfolio_cli_2_topic"></a>

The following code example shows how to use `update-portfolio`.

**AWS CLI**
**To update a portfolio**
The following `update-portfolio` example updates the name of the specified portfolio.

```
aws servicecatalog update-portfolio \
    --id {{port-5abcd3e5st4ei}} \
    --display-name {{"New portfolio name"}}
```
Output:

```
{
    "PortfolioDetail": {
        "DisplayName": "New portfolio name",
        "ProviderName": "provider",
        "ARN": "arn:aws:catalog:us-west-2:123456789012:portfolio/port-5abcd3e5st4ei",
        "Id": "port-5abcd3e5st4ei",
        "CreatedTime": 1559665256.348
    },
    "Tags": []
}
```
+  For API details, see [UpdatePortfolio](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/update-portfolio.html) in *AWS CLI Command Reference*.

### `update-product`
<a name="service-catalog_UpdateProduct_cli_2_topic"></a>

The following code example shows how to use `update-product`.

**AWS CLI**
**To update a product**
The following `update-product` example updates the name and owner of the specified product.

```
aws servicecatalog update-product \
    --id {{prod-os6abc7drqlt2}} \
    --name {{"New product name"}} \
    --owner {{"Updated product owner"}}
```
Output:

```
{
    "Tags": [
        {
            "Value": "iad",
            "Key": "region"
        }
    ],
    "ProductViewDetail": {
        "ProductViewSummary": {
            "Owner": "Updated product owner",
            "ProductId": "prod-os6abc7drqlt2",
            "Distributor": "test-distributor",
            "SupportUrl": "https://aws.amazon.com",
            "Name": "New product name",
            "ShortDescription": "test-description",
            "HasDefaultPath": false,
            "Id": "prodview-6abcdgrfhvidy",
            "SupportDescription": "test-support",
            "SupportEmail": "test@amazon.com",
            "Type": "CLOUD_FORMATION_TEMPLATE"
        },
        "Status": "CREATED",
        "ProductARN": "arn:aws:catalog:us-west-2:123456789012:product/prod-os6abc7drqlt2",
        "CreatedTime": 1577136255.0
    }
}
```
+  For API details, see [UpdateProduct](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/update-product.html) in *AWS CLI Command Reference*.

### `update-provisioning-artifact`
<a name="service-catalog_UpdateProvisioningArtifact_cli_2_topic"></a>

The following code example shows how to use `update-provisioning-artifact`.

**AWS CLI**
**To update a provisioning artifact**
The following `update-provisioning-artifact` example updates the name and description of the specified provisioning artifact, using a JSON file to pass parameters.

```
aws servicecatalog update-provisioning-artifact \
    --cli-input-json {{file://update-provisioning-artifact-input.json}}
```
Contents of `update-provisioning-artifact-input.json`:

```
{
    "ProductId": "prod-abcdfz3syn2rg",
    "ProvisioningArtifactId": "pa-pcz347abcdcfm",
    "Name": "updated name",
    "Description": "updated description"
}
```
Output:

```
{
    "Info": {
        "TemplateUrl": "https://awsdocs.s3.amazonaws.com/servicecatalog/myexampledevelopment-environment.template"
    },
    "Status": "AVAILABLE",
    "ProvisioningArtifactDetail": {
        "Active": true,
        "Description": "updated description",
        "Id": "pa-pcz347abcdcfm",
        "Name": "updated name",
        "Type": "CLOUD_FORMATION_TEMPLATE",
        "CreatedTime": 1562097906.0
    }
}
```
+  For API details, see [UpdateProvisioningArtifact](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/update-provisioning-artifact.html) in *AWS CLI Command Reference*.

### `update-tag-option`
<a name="service-catalog_UpdateTagOption_cli_2_topic"></a>

The following code example shows how to use `update-tag-option`.

**AWS CLI**
**To update a TagOption**
The following `update-tag-option` example updates the value of a `TagOption`, using the specified JSON file.

```
aws servicecatalog update-tag-option --cli-input-json {{file://update-tag-option-input.json}}
```
Contents of `update-tag-option-input.json`:

```
{
    "Id": "tag-iabcdn4fzjjms",
    "Value": "newvalue",
    "Active": true
}
```
Output:

```
{
    "TagOptionDetail": {
        "Value": "newvalue",
        "Key": "1234",
        "Active": true,
        "Id": "tag-iabcdn4fzjjms"
    }
}
```
+  For API details, see [UpdateTagOption](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog/update-tag-option.html) in *AWS CLI Command Reference*.
