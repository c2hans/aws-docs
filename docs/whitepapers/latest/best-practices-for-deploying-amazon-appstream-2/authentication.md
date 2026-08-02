---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/authentication.html
---

# Authentication
<a name="authentication"></a>

 With WorkSpaces Applications, authentication can either take place outside of Amazon WorkSpaces Applications, or as part of the WorkSpaces Applications service. Selecting how authentication will take place for your WorkSpaces Applications deployment is a fundamental consideration of your design. It’s not uncommon for an organization to have multiple deployments of WorkSpaces Applications for different use-cases. Each use-case can have a different authentication method.

 There are three types of authentication methods for WorkSpaces Applications:
+  [https://en.wikipedia.org/wiki/SAML_2.0](https://en.wikipedia.org/wiki/SAML_2.0)
+  [https://docs.aws.amazon.com/cognito/latest/developerguide/authentication.html](https://docs.aws.amazon.com/cognito/latest/developerguide/authentication.html)
+  Programmatic

## Determining optimized method
<a name="determining-optimized-method"></a>

 Amazon WorkSpaces Applications is architected to be flexible to apply to most organizational design requirements. When determining the optimized method for authentication, it is a best practice to consider the objectives and purposes of those who consume the service, and the organizational policies and procedures.

 Here are some examples of combining use-cases with organizational objectives.

 *Table 4 — Use cases with organizational objectives*

|  **Example**  |  **Description**  |  **Authentication**  |
| --- | --- | --- |
|  Domain joined fleet instances are required  |  Applications installed on the WorkSpaces Applications image are accessible only to domain joined resources.  |  SAML 2.0  |
|  Heavy integration with Microsoft services  |  Organizational dependence on developing Microsoft Group Policies and backend infrastructure  |  SAML 2.0  |
|  Existing enterprise Single Sign-on (SSO)  |  All new services must leverage an enterprise SSO solution that has several reporting and security processes established.  |  SAML 2.0  |
|  Smart card support for applications  |  Smart cards (such as Private Identity Verification and common access cards) for in-session authentication to streamed applications through a smart card reader.  |  SAML 2.0  |
|  Seasonal workforce with temporary staffing  |  A few months out of the year, temporary workers are assigned a small set of applications that do not include internal resources to complete activities.  |  User Pool  |
|  Limited IT Support  |  Smaller organizations with less than 50 users and limited IT staff, looking to remove the overhead of maintaining an Identity Provider (IdP)  |  User Pool  |
|  Independent Software Vendor (ISV)  |  Proprietary solution built by your organization that includes user entitlement and authentication, extending WorkSpaces Applications as part of your solution.\*  |  Programmatic  |
|  Technology showcase  |  Completely ephemeral environment that showcases a proprietary technology as part of a guided tour of your solution with no requirement to store user information.  |  Programmatic  |
|  Interactive website experience  |  Make your website interactive with streaming Windows applications.\*\*  |  Programmatic  |

 \*Refer to [https://aws.amazon.com/appstream2/getting-started/isv-workshops/](https://aws.amazon.com/appstream2/getting-started/isv-workshops/) for more information.

 \*\*Refer to [https://docs.aws.amazon.com/appstream2/latest/developerguide/embed-streaming-sessions.html](https://docs.aws.amazon.com/appstream2/latest/developerguide/embed-streaming-sessions.html) for more information.

 If your organization has a use-case or policy that is not listed in the examples previously given, it is a best practice to forecast the desired end state of WorkSpaces Applications workflow consumption to ensure the authentication solution does not conflict with it.

## Configuring your identity provider
<a name="configuring-your-identity-provider"></a>

### SAML 2.0
<a name="saml-2.0"></a>

 Security Assertion Markup Language (SAML) 2.0 is a common deployment option for [https://aws.amazon.com/identity/saml/](https://aws.amazon.com/identity/saml/). Various [https://docs.aws.amazon.com/appstream2/latest/developerguide/external-identity-providers-further-info.html](https://docs.aws.amazon.com/appstream2/latest/developerguide/external-identity-providers-further-info.html) support WorkSpaces Applications . Whether your WorkSpaces Applications resources are domain joined or not, SAML 2.0 IdP requires you to use [ IAM](https://aws.amazon.com/iam/).

As most IdPs generate a unique metadata.xml with specific SAML attributes for each SAML application, every WorkSpaces Applications stack requires a Role that has a trusted relationship with the SAML IdP and a Policy that has a single permission to appstream:Stream with conditions that match the requirements of the SAML IdP and the ARN of the WorkSpaces Applications Stack.

The WorkSpaces Applications administration guide provides an example configuration for single WorkSpaces Applications stack design. For multiple stack deployments, refer to the optional steps for using [SAML 2.0 multi-stack application catalog](https://docs.aws.amazon.com/appstream2/latest/developerguide/application-entitlements-saml.html#saml-application-catalog).

### User pool
<a name="user-pool"></a>

 The **User Pool** tab in WorkSpaces Applications is a valid option for small proof of concepts. As a best practice, it is best to avoid user pools for any use case and organization that uses WorkSpaces Applications to deliver production applications.

 One important thing to note about user pools is that users’ email addresses are case-sensitive; therefore it is a best practice to ensure users are educated on how to properly enter user credentials.

### Streaming url
<a name="streaming-url"></a>

 For deployments that call WorkSpaces Applications resources from a centralized service (typically ISVs), programmatic authentication relies on an application to make programmatic calls to AWS to dynamically pass information and create a WorkSpaces Applications session for its users. Use the API authentication method (commonly referred to as ‘programmatic’) when creating streaming URLs using the [https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateStreamingURL.html](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateStreamingURL.html) operation. The user who makes the `CreateStreamingURL` call must be using a valid user or role with permission for `appstream:CreateStreamingURL`.

 When creating the policy for programmatic access, it is a best practice to secure access by specifying the exact WorkSpaces Applications Stack ARN in the **Resources** section in place of the default ‘\*’. For example:

**Example**
****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "appstream:createStreamingURL"
            ],
            "Resource": "arn:aws:appstream:us-east-1:031421429609:stack/BestPracticesStack"
        }
    ]
}
```

**Note**
You can quickly retrieve the ARNs of your WorkSpaces Applications Stacks by using the describe stacks [API](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_DescribeStacks.html) or [AWS CLI](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appstream/describe-stacks.html).

 WorkSpaces Applications instances should start as generic instances. Through information passed to it from the application, the WorkSpaces Applications instance establishes the environment using [https://docs.aws.amazon.com/appstream2/latest/developerguide/managing-stacks-fleets.html#managing-stacks-fleets-parameters](https://docs.aws.amazon.com/appstream2/latest/developerguide/managing-stacks-fleets.html#managing-stacks-fleets-parameters) to make things dynamic for the user.

 While local GPOs can be used to specify settings at user logon, session context is a best practice when using `CreateStreamingURL`, and passing key attributes such as Customer ID or database connection settings, to be used in the WorkSpaces Applications session.

### Application entitlement
<a name="application-entitlement"></a>

WorkSpaces Applications can dynamically build the application catalog that is presented to users. Application entitlements are based on SAML 2.0 attributes, or by using WorkSpaces Applications Dynamic Application Framework.

Attribute-based application entitlements using SAML 2.0 is recommended in most scenarios. To manage application package delivery, Dynamic Application Framework is recommended.
