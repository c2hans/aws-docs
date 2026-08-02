---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-gen-ai-selling-partner-api/integrating-sp-api.html
---

# Integrating the Amazon Selling Partner API
<a name="integrating-sp-api"></a>

In order to access the data through the Amazon Selling Partner API (SP-API), you must complete the following actions:

1. [Register as an SP-API developer](#integrating-developer)

1. [Request SP-API roles](#integrating-roles)

1. [Register your application](#integrating-register)

1. [Select an authorization model for your application](#integrating-authorization)

1. [Connect to the SP-API](#integrating-connect)

## Register as an SP-API developer
<a name="integrating-developer"></a>

Before you can register your SP-API application, you must create an Amazon developer account and register as an SP-API developer. For a comprehensive overview of the developer registration process, see [SP-API Registration Overview](https://developer-docs.amazon.com/sp-api/docs/sp-api-registration-overview) in the SP-API documentation.

## Request SP-API roles
<a name="integrating-roles"></a>

An [SP-API role](https://developer-docs.amazon.com/sp-api/docs/roles-in-the-selling-partner-api) determines whether a developer or application has access to a specific operation or resource. As a developer, you must request and qualify for a particular role, or you will not be able to access the operations and resources grouped under that role.

Roles protect access to personally identifiable information (PII) and other sensitive data. They limit data access to make sure that developers can access only the data that is required for their application. This helps protect customer data and preserve customer trust.

Accessing the data available in the brand analytics reports requires that you have the [Brand Analytics role](https://developer-docs.amazon.com/sp-api/docs/brand-analytics-role). For more information about requesting access to a role, see [How do I request and qualify for a role](https://developer-docs.amazon.com/sp-api/docs/roles-in-the-selling-partner-api#how-do-i-request-and-qualify-for-a-role) in the SP-API documentation.

## Register your application
<a name="integrating-register"></a>

The registration process varies slightly depending on the application type. For the purposes of registration, applications are categorized as one of the following types:
+ **Public applications and private seller applications** ­– These are applications that are publicly available and are authorized by a seller or vendor, or they are seller applications that are available only to your organization and are self-authorized.
+ **Private vendor applications** – These are vendor applications that are available only to your organization and are self-authorized.

For more information, see [Register your application](https://developer-docs.amazon.com/sp-api/docs/registering-your-application) in the SP-API documentation.

## Select an authorization model for your application
<a name="integrating-authorization"></a>

The authorization model for the Selling Partner API is based on [Login with Amazon](https://developer.amazon.com/docs/login-with-amazon/documentation-overview.html), an Amazon implementation of OAuth 2.0. Your application is authorized through interactions with pages displayed by Amazon and your website. The web browser is the user-agent that passes parameters between your website and Amazon at each selling partner action. To implement OAuth authorization, you must configure your website to accept and process the parameters that Amazon passes to it. You must also configure your website to redirect the web browser and pass parameters to Amazon. For more information about authorization, see [Authorizing Selling Partner API applications](https://developer-docs.amazon.com/sp-api/docs/authorizing-selling-partner-api-applications) in the SP-API documentation.

### Understand application authorization
<a name="understand-application-authorization.9b808de3-377a-53c7-b52f-acc58dc3cb70"></a>

For the purposes of authorization, there are three types of applications:
+ **Public applications for sellers** – These applications are publicly available and are authorized by sellers. You can choose one of the following authorization workflows:
  + [Selling Partner Appstore authorization workflow](https://developer-docs.amazon.com/sp-api/docs/selling-partner-appstore-authorization-workflow) – An OAuth authorization workflow that is initiated from the Selling Partner Appstore detail page.
  + [Website authorization workflow](https://developer-docs.amazon.com/sp-api/docs/website-authorization-workflow) – An OAuth authorization workflow that is initiated from your own website.
+ **Public applications for vendors** – These applications are publicly available and are authorized by vendors. You can use the [Website authorization workflow](https://developer-docs.amazon.com/sp-api/docs/website-authorization-workflow). This is an OAuth authorization workflow that is initiated from your own website.
+ **Private applications for sellers or vendors** – These applications are available only to your organization. These can be seller or vendor applications. You can use the [Self authorization](https://developer-docs.amazon.com/sp-api/docs/self-authorization) approach. When you create a private application for your own organization you can self-authorize it to access your account information. You can self-authorize your application in draft status; there is no reason to publish a private application. For information about revoking self-authorization from seller and vendor applications, see [Revoke self-authorizations](https://developer-docs.amazon.com/sp-api/docs/revoke-self-authorizations-from-your-application) in the SP-API documentation.

### Authorize vendor groups for application access
<a name="authorize-vendor-groups-for-application-access.b40ad6d6-2949-5d2c-a851-87d784fede1f"></a>

When you authorize your Selling Partner API application to access your data, you are granting access to the vendor group that is associated with the sign-in credentials for your Vendor Central account. By extension, you are granting access to all vendor codes that are present in the vendor group. Therefore, it's important to use the right Vendor Central credentials and vendor group for your Selling Partner API integration.

The *vendor group* is the account you log in to. Depending on your business agreements, operation models, and other factors, your vendor group can include one or more vendor codes. Each *vendor code* allows you to list products in a specific category, or it includes the necessary business agreements, such as one vendor code for a particular brand.

You can [have multiple authorizations](https://developer-docs.amazon.com/sp-api/docs/authorize-vendor-groups-for-application-access#use-multiple-vendor-groups-to-authorize-an-application) for each vendor group, or you can create a [single vendor group](https://developer-docs.amazon.com/sp-api/docs/authorize-vendor-groups-for-application-access#use-a-single-vendor-group-to-authorize-an-application) that contains all of your vendor codes. The option to use multiple vendor groups that are associated with your profile gives you the ability to use an application with the same vendor code in different vendor groups. With this option, you don't have to submit multiple vendor developer applications for each vendor group.

For more information, see [Authorize vendor groups for application access](https://developer-docs.amazon.com/sp-api/docs/authorize-vendor-groups-for-application-access) in the SP-API documentation.

## Connect to the SP-API
<a name="integrating-connect"></a>

After you have registered and authorized your application, you can start making requests. For more information, see [Connecting to the Selling Partner API](https://developer-docs.amazon.com/sp-api/docs/connecting-to-the-selling-partner-api) in the SP-API documentation.
