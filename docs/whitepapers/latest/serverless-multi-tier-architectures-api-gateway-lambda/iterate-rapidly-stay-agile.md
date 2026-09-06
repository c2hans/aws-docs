---
source_url: https://docs.aws.amazon.com/whitepapers/latest/serverless-multi-tier-architectures-api-gateway-lambda/iterate-rapidly-stay-agile.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Iterate rapidly, stay agile
<a name="iterate-rapidly-stay-agile"></a>

 Using Amazon API Gateway and AWS Lambda to build the logic tier of your API enables you to quickly adapt to the changing demands of your user base by simplifying API deployment and version management.

## Stage deployment
<a name="stage-deployment"></a>

 When you deploy an API in API Gateway, you must associate the deployment with an API Gateway stage – each stage is a snapshot of the API and is made available for client apps to call. Using this convention, you can easily deploy apps to *dev*, *test*, *stage*, or *prod* stages, and move deployments between stages. Each time you deploy your API to a stage, you create a different version of the API which can be reverted if necessary. These features enable existing functionality and client dependencies to continue undisturbed while new functionality is released as a separate API version.

## Decoupled integration with Lambda
<a name="decoupled-integration-with-lambda"></a>

 The integration between API in API Gateway and Lambda function can be decoupled using API Gateway stage variables and a Lambda function alias. This simplifies and speeds up the API deployment. Instead of configuring the Lambda function name or alias in the API directly, you can configure stage variable in API which can point to a particular alias in the Lambda function. During deployment, change the stage variable value to point to a Lambda function alias and API will run the Lambda function version behind the Lambda alias for a particular stage.

## Canary release deployment
<a name="canary-release-deployment"></a>

Canary release is a software development strategy in which a new version of an API is deployed for testing purposes, and the base version remains deployed as a production release for normal operations on the same stage. In a canary release deployment, total API traffic is separated at random into a production release and a canary release with a preconfigured ratio. APIs in API Gateway can be configured for the canary release deployment to test new features with a limited set of users.

## Custom domain names
<a name="custom-domain-names"></a>

You can provide an intuitive business-friendly URL name to API instead of the URL provided by API Gateway. API Gateway provides features to configure custom domain for the APIs. With custom domain names, you can set up your API's hostname, and choose a multi-level base path (for example, `myservice`, `myservice/cat/v1`, or `myservice/dog/v2`) to map the alternative URL to your API.
