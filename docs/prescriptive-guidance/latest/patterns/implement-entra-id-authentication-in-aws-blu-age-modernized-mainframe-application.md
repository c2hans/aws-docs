---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-entra-id-authentication-in-aws-blu-age-modernized-mainframe-application.html
---

# Implement Microsoft Entra ID-based authentication in an AWS Blu Age modernized mainframe application
<a name="implement-entra-id-authentication-in-aws-blu-age-modernized-mainframe-application"></a>

*Vishal Jaswani and Rimpy Tewani, Amazon Web Services*

## Summary
<a name="implement-entra-id-authentication-in-aws-blu-age-modernized-mainframe-application-summary"></a>

**Note**
AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

Mainframe applications that are modernized by using refactoring patterns, such as those by [AWS Mainframe Modernization Refactor with AWS Blu Age](https://docs.aws.amazon.com/m2/latest/userguide/refactoring-m2.html), require careful integration of authentication mechanisms into the new application architecture. This integration is typically addressed as a post-modernization activity. The task can be complex and often involves the migration or externalization of existing authentication systems to align with modern security standards and cloud-native practices. Developers need to consider how to implement authentication effectively while they work within the constraints of the modernized application's runtime environment and libraries. After modernization, AWS provides ways to make it easier for you to integrate your AWS Blu Age modern code with identity and access management systems such as [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) and [Microsoft Entra ID](https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id) (formerly known as Azure AD).

This pattern explains how to implement an authentication mechanism in your modernized application when the authentication provider is Microsoft Entra ID, without spending time on research and trials. The pattern provides:
+ Field-tested and relevant Angular libraries from the Microsoft Authentication Library (MSAL) and other Microsoft Entra ID documentation that are essential to the authentication implementation.
+ Configurations required on the AWS Blu Age Runtime to enable Spring Security by using OAuth 2.0.
+ A library that captures authenticated users’ identities and passes them to the AWS Blu Age Runtime.
+ Security measures that we recommend implementing.
+ Troubleshooting tips for commonly encountered problems with the Microsoft Entra ID setup.

**Note**
This pattern uses the AWS Blu Age OAuth extension library, which is provided to customers as part of their [AWS Professional Services](https://aws.amazon.com/professional-services/) engagement. This library isn’t part of the AWS Blu Age Runtime.

## Prerequisites and limitations
<a name="implement-entra-id-authentication-in-aws-blu-age-modernized-mainframe-application-prereqs"></a>

**Prerequisites**
+ A modernized application that was produced by AWS Blu Age mainframe modernization refactoring tools. This pattern uses [CardDemo](https://github.com/aws-samples/aws-mainframe-modernization-carddemo) as a sample open source mainframe application.
+ The AWS Blu Age OAuth extension library, which is provided by the AWS Blu Age team during your engagement with [AWS Professional Services](https://aws.amazon.com/professional-services/).
+ An active AWS account to deploy and test the modernized application.
+ Familiarity with AWS Blu Age configuration files and Microsoft Entra ID fundamentals.

**Limitations**
+ This pattern covers OAuth 2.0 authentication and basic token-based authorization flows. Advanced authorization scenarios and fine-grained access control mechanisms are not in scope.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.

**Product versions**

This pattern was developed by using:
+ AWS Blu Age Runtime version 4.1.0 (the pattern also works with later versions that are backward compatible)
+ MSAL library version 3.0.23
+ Java Development Kit (JDK) version 17
+ Angular version 16.1

## Architecture
<a name="implement-entra-id-authentication-in-aws-blu-age-modernized-mainframe-application-architecture"></a>

**Source technology stack**

In typical mainframe environments, authentication is implemented through user profiles. These profiles identify users to the system, define who can sign in, and specify which functions users can perform on system resources. User profiles are managed by security officers or security administrators.

**Target technology stack**
+ Microsoft Entra ID
+ Modernized Java Spring Boot-based backend
+ AWS Blu Age Runtime
+ Spring Security with OAuth 2.0
+ Angular single-page application (SPA)

**Target architecture**

AWS Blu Age runtime supports OAuth 2.0-based authentication by default, so the pattern uses that standard to protect backend APIs.

The following diagram illustrates the process flow.

**Note**
The diagram includes Amazon Aurora as an example of database modernization although Aurora isn’t included in the steps for this pattern.

![Process flow for Entra ID-based authentication for an AWS Blu Age application.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/e51f24b8-178f-4974-aae9-23a0cc8540f5/images/0fdcdb22-9e46-4b02-86b2-395cba3e2f81.png)

where:

1. A user tries to authenticate with Microsoft Entra ID.

1. Microsoft Entra ID returns refresh, access, and ID tokens that the application uses in subsequent calls.

1. The MSAL interceptor includes the access token in the `Authorization` header of an HTTPS request to call the AWS Blu Age Runtime.

1. The AWS Blu Age `extension-oauth` library extracts the user information from the header by using an AWS Blu Age Runtime configuration file (`application-main.yml`) and places this information in a `SharedContext` object so that the business logic can consume it.
**Note**
`SharedContext` is a runtime component provided by AWS Blu Age that manages application context and state information across the modernized application. For more information about AWS Blu Age Runtime components and updates, see [AWS Blu Age release notes](https://docs.aws.amazon.com/m2/latest/userguide/ba-release-notes.html) in the AWS Mainframe Modernization documentation. For more information about the `application-main.yml` file, see [Set up configuration for AWS Blu Age Runtime](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-config.html) in the AWS Mainframe Modernization documentation.

1. The AWS Blu Age Runtime checks if the token is present.

   1. If the token is present, it checks the validity of the token by communicating with Microsoft Entra ID.

   1. If the token isn’t present, the AWS Blu Age Runtime returns an error with HTTP status code 403.

1. If the token is valid, the AWS Blue Age Runtime allows the business logic to continue. If the token is invalid, the AWS Blu Age Runtime returns an error with HTTP status code 403.

**OAuth 2.0 workflow**

For a high-level diagram of the OAuth 2.0 workflow, see the [Microsoft Entra documentation](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow#protocol-details).

## Tools
<a name="implement-entra-id-authentication-in-aws-blu-age-modernized-mainframe-application-tools"></a>

**AWS services**

[AWS Mainframe Modernization](https://docs.aws.amazon.com/m2/latest/userguide/what-is-m2.html) provides tools and resources to help you plan and implement migration and modernization from mainframes to AWS managed runtime environments. You can use this service’s refactoring features, which are provided by AWS Blu Age, to convert and modernize your legacy mainframe applications.

**Note**
AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

**Code repository**

The CardDemo application has been updated to demonstrate integration with Microsoft Entra ID. You can access the code from the [GitHub repository for this pattern](https://github.com/aws-samples/sample-microsoft-entra-id-based-auth-in-aws-bluage-modernized-mainframe-app).

**Backend configuration**

This pattern requires changes to the `application-main.yml`** **configuration file to enable Spring Security by using OAuth 2.0 on the backend application.  The `.yml` file looks like this:

```
gapwalk-application.security: enabled
gapwalk-application:
  security:
    identity: oauth
    issuerUri: ${issuerUrl}
    claim:
      claims:
        -
          claimName: upn
          claimMapValue: username
spring:
  autoconfigure:
    exclude:
     - org.springframework.boot.autoconfigure.security.oauth2.client.servlet.OAuth2ClientAutoConfiguration
     - org.springframework.boot.autoconfigure.security.oauth2.resource.servlet.OAuth2ResourceServerAutoConfiguration
  security:
    oauth2:
      client:
        registration:
          azure:
            client-id: {clientId}
            client-secret: ${clientSecret}
            provider: azure
            authorization-grant-type: authorization_code
            redirect-uri: ${redirectUri}
            scope: openid

        provider:
          azure:
            authorization-uri: ${gapwalk-application.security.issuerUri}/oauth2/v2.0/authorize
            token-uri:  ${gapwalk-application.security.issuerUri}/oauth2/v2.0/token
            jwk-set-uri: ${gapwalk-application.security.issuerUri}/discovery/v2.0/keys
      resourceserver:
        jwt:
          jwk-set-uri: ${gapwalk-application.security.issuerUri}/discovery/v2.0/keys
```

**AWS Blu Age OAuth extension filter library**

The AWS Blu Age OAuth extension library is provided by the AWS Blu Age team during your engagement with [AWS Professional Services](https://aws.amazon.com/professional-services/).

This library reads the `claim.claims` configuration in the `application-main.yml` fie that’s shown in the previous code block. This configuration is a list. Each item in the list provides two values: `claimName` and `claimMapValue`. `claimName` represents a key name in a JSON Web Token (JWT) sent by the frontend, and `claimMapValue` is the name of the key in `SharedContext`. For example, if you want to capture the user ID on the backend, set `claimName` to the key name in the JWT that holds the `userId` that’s provided by Microsoft Entra ID, and set `claimMapValue` to the key name to fetch the user ID in the backend code.

For example, if you set `UserId` in `claimMapValue`, you can use the following code  to extract the user ID:

```
SharedContext.get().getValue("userId", [UserId]);
```

## Best practices
<a name="implement-entra-id-authentication-in-aws-blu-age-modernized-mainframe-application-best-practices"></a>

In your implementation of this pattern, take the following important security considerations into account.

**Important**
This pattern provides a foundation for authentication integration. We recommend that you implement security measures in addition to those discussed in this section based on your business requirements before you deploy it to production.
+ **AWS configuration security. **Move sensitive configuration values from `application-main.yml` to AWS Secrets Manager. For example, configure the following properties by using Secrets Manager:

  ```
  security:
      oauth2:
        client:
          registration:
            azure:
              client-id: {clientId}
              client-secret: ${clientSecret}
  ```

  For more information about how you can use Secrets Manager to configure AWS Blu Age parameters, see [AWS Blu Age Runtime secrets](https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-config-app-secrets.html) in the AWS Mainframe Modernization documentation.
+ **Runtime environment protection.** Configure the modernized application environment with proper AWS security controls:

  ```
  server:
    tomcat:
      remoteip:
       protocol-header: X-Forwarded-Proto
       remote-ip-header: X-Forwarded-For
    forward-headers-strategy: NATIVE
  ```
+ **Amazon CloudWatch logging.** Consider adding the file `logback-spring.xml to src/main/resources`:

  ```
  <configuration>
   <appender name="CLOUDWATCH" class="com.amazonaws.services.logs.logback.CloudWatchAppender">
     <logGroup>/aws/bluage/application</logGroup>
     <logStream>${AWS_REGION}-${ENVIRONMENT}</logStream>
     <layout>
      <pattern>%d{yyyy-MM-dd HH:mm:ss} [%thread] %-5level %logger{36} - %msg%n</pattern>
     </layout>
   </appender>

   <root level="INFO">
   <appender-ref ref="CLOUDWATCH"/>
   </root>
  </configuration>
  ```

  For information about enabling tracing with CloudWatch, see [Enable trace to log correlation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Application-Signals-TraceLogCorrelation.html) in the CloudWatch documentation.
+ **Token configuration and handling.** Configure token lifetimes in Microsoft Entra ID to align with your security requirements. Set access tokens to expire within 1 hour and refresh tokens to expire within 24 hours. In the AWS Blu Age Runtime configuration (`application-main.yml`), make sure that JWT validation is configured properly with the exact issuer URI and audience values from your Entra ID application registration.

  When a token expires and is refreshed:

  1. The Angular application's error interceptor handles the 401 response by obtaining a new token through MSAL.

  1. The new token is sent with the subsequent request.

  1. The AWS Blu Age Runtime's OAuth filter validates the new token and automatically updates `SharedContext` with the current user information. This ensures that business logic continues to have access to valid user context through `SharedContext.get().getValue()` calls.

  For more information about the AWS Blu Age Runtime components and their updates, see [AWS Blu Age release notes](https://docs.aws.amazon.com/m2/latest/userguide/ba-release-notes.html).
+ **AWS Blu Age Runtime security.** The `oauth2-ext` library provided by AWS Blu Age must be placed in the correct shared directory location (`{app-server-home}/shared/`) with proper file permissions. Verify that the library successfully extracts user information from JWTs by checking the `SharedContext` object population in your logs.
+ **Specific claims configuration.** In `application-main.yml`, define the claims that you need from Microsoft Entra ID explicitly. For example, to capture the user's email and roles, specify:

  ```
  gapwalk-application:
    security:
      claim:
        claims:
          - claimName: upn
            claimMapValue: username
          - claimName: roles
            claimMapValue: userRoles
          - claimName: email
            claimMapValue: userEmail
  ```
+ **Error handling.** Add error handling to address authentication failures in your Angular application; for example:

  ```
  @Injectable()
  export class AuthErrorInterceptor implements HttpInterceptor {
    intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
      return next.handle(request).pipe(
        catchError((error: HttpErrorResponse) => {
          if (error.status === 401) {
            // Handle token expiration
            this.authService.login();
          }
          if (error.status === 403) {
            // Handle unauthorized access
            this.router.navigate(['/unauthorized']);
          }
          return throwError(() => error);
        })
      );
    }
  }
  ```
+ **Session timeout configuration.** Configure session timeout settings in both the AWS Blu Age Runtime and Microsoft Entra ID. For example, add the following code to your `application-main.yml` file:

  ```
  server:
    servlet:
      session:
        timeout: 3600 # 1 hour in seconds
  ```
+ **MsalGuard.** You must implement the MsalGuard feature for all protected routes to prevent unauthorized access. For example:

  ```
  const routes: Routes = [
      { path: '', redirectTo: '/transaction-runner', pathMatch: 'full' },
      { path: 'transaction-runner', component: TransactionRunnerComponent, canActivate:guards },
      { path: 'user-info', component: UserInfoComponent, canActivate:guards },
      { path: 'term/:transid/:commarea', component: TermComponent, canActivate:guards },
  	{ path: 'code', component: TransactionRunnerComponent  }
  ];
  ```

  Routes that don’t have MsalGuard protection will be accessible without authentication, potentially exposing sensitive functionality. Make sure that all routes that require authentication include the guards in their configuration.

## Epics
<a name="implement-entra-id-authentication-in-aws-blu-age-modernized-mainframe-application-epics"></a>

### Set up a Microsoft Entra ID
<a name="set-up-a-microsoft-entra-id"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up a Microsoft Azure account to create an Entra ID. | For options and instructions, see the [Microsoft Azure website](https://azure.microsoft.com/en-us/free/). | App developer |
| Set up a Microsoft Entra ID in your application. | To learn how to add Microsoft Entra ID B2C (Azure AD B2C) authentication to your Angular SPA, see the [Microsoft documentation](https://learn.microsoft.com/en-us/azure/active-directory-b2c/enable-authentication-angular-spa-app#add-the-authentication-components). Specifically:1. [Register your application and record identifiers](https://learn.microsoft.com/en-us/entra/identity-platform/tutorial-v2-angular-auth-code#register-the-application-and-record-identifiers).<br />2. Expose the AWS Blu Age transaction endpoint by [adding and exposing a custom scope](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-configure-app-expose-web-apis#add-a-scope).  <br />3. After you define the scope and the API URL, configure these values in the `apiUri` and `apiScope` properties of the `environment.ts` file in the code repository. | App developer |

### Clone the repository and deploy your AWS Blu Age code
<a name="clone-the-repository-and-deploy-your-aws-blu-age-code"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the GitHub repository to get the Angular code required for authentication. | Run the following command to clone the [GitHub repository](https://github.com/aws-samples/sample-microsoft-entra-id-based-auth-in-aws-bluage-modernized-mainframe-app) that’s provided with this pattern into your local current working directory:<pre>git clone https://github.com/aws-samples/sample-microsoft-entra-id-based-auth-in-aws-bluage-modernized-mainframe-app.git</pre> | App developer |
| Deploy the AWS Blu Age modernized code on a Tomcat server to implement authentication. | To set up the local environment that includes Tomcat and the Angular development server, follow the installation steps provided by the AWS Blu Age team as part of your customer engagement with AWS Professional Services. | App developer |

### Build the authentication solution
<a name="build-the-authentication-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Enable AWS Blu Age Runtime security to protect the AWS Blu Age REST API endpoints. | Configure the `application-main.yml` file that the AWS Blu Age Runtime uses as follows. For an example of this file, see the [Code repository](#implement-entra-id-authentication-in-aws-blu-age-modernized-mainframe-application-tools) section earlier in this pattern.+ `spring:security:oauth2:client:*` enables Spring Security OAuth 2.0 client support. Replace the settings with values that are specific to your Microsoft Entra ID setup.<br />+ `spring:security:oauth2:resourceserver` enables Spring Security OAuth 2.0 resource server support.<br />+ `gapwalk-application.security.issuerUri` specifies the URL of the identity provider for fetching configuration information such as the authorization endpoint, the token endpoint, and so on.<br />+ `gapwalk-application.security.identity` should be set to `oauth`.<br />+ `gapwalk-application.security.claim.claims` specifies the list of claims required to capture user IDs and user names.  For an example, see the [Code repository](#implement-entra-id-authentication-in-aws-blu-age-modernized-mainframe-application-tools) section earlier in this pattern.<br />+ `gapwalk-application.security` should be set to `enabled`.<br />+ `spring.autoconfigure.exclude` should be removed to enable authentication. | App developer |
| Incorporate the example code from your local environment into your Blu Age modernized Angular code base. | For information about how to incorporate the example into your AWS Blu Age modernized Angular code base, see the [Code repository](#implement-entra-id-authentication-in-aws-blu-age-modernized-mainframe-application-tools) section earlier in this pattern. | App developer |
| Place the `oauth2-ext` library in the shared directory. | Place the `oauth2-ext` library in the** **shared directory of the application server so that your** **AWS Blu Age modernized application can use it**. **Run the following commands:<pre>cd oauth2-ext/target<br />cp extension-oauth-filter-<version>.jar /{app-server-home}/shared/</pre> | App developer |

### Deploy the authentication solution
<a name="deploy-the-authentication-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the frontend application. | Run the following commands to start the frontend application locally:<pre>npm install <br />ng serve --ssl<br />npm start</pre>Adding the `--ssl` flag to the `ng serve` command ensures that the development server uses HTTPS, which is more secure than other protocols and provides a better simulation of a production environment. | App developer |
| Start the backend application. | Start Tomcat server in Eclipse. | App developer |

### Test the application
<a name="test-the-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Test login functionality. | Access the locally deployed application at `http://localhost:4200` to verify that users are asked to confirm their identity.HTTP is used here for demonstration purposes. In a production or other publicly accessible environment, you must use HTTPS for security. Even for local development, we recommend that you set up HTTPS when possible.<br />The Microsoft login prompt should appear, and users who are configured in Microsoft Entra ID should be allowed to access the application. | App developer |
| Test the authorization header in the request. | The following steps use the [CardDemo](https://github.com/aws-samples/aws-mainframe-modernization-carddemo) application as an example. Testing steps for other modern applications will vary.1. Launch transaction `CC00` in the CardDemo application.<br />2. Sign in with user credentials. For example, if you’re using the [AWS Blu Age level 3 self-paced workshop](https://catalog.workshops.aws/aws-blu-age-l3-certification-workshop/en-US/execution/test/online/user-features), you can use the name `USER0001` and password `PASSWORD` for credentials.<br />3. Open the **Developer Tools** window in the same tab of your browser.<br />4. Open the **Network** tab and check the request sent to the backend `http://localhost:8080/gapwalk-application/transaction`.<br />5. Check the request header and verify that you see an authorization header with the value `Bearer <token>` where `<token>` is a value that’s generated by Microsoft Entra ID. | App developer |
| Test the logout functionality. | Choose **Quit** to log out, and try to access the application again. It should present a new login prompt. | App developer |

## Troubleshooting
<a name="implement-entra-id-authentication-in-aws-blu-age-modernized-mainframe-application-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| The token issued by Microsoft Entra ID isn’t compatible with Spring Boot OAuth 2.0 security. | For a resolution to the issue, see [Microsoft Entra ID OAuth Flow](https://authguidance.com/azure-ad-troubleshooting/) on the OAuth blog. |
| General token-related questions. | To decode and view the contents of a JWT token, use the [https://jwt.io/](https://jwt.io/) website. |

## Related resources
<a name="implement-entra-id-authentication-in-aws-blu-age-modernized-mainframe-application-resources"></a>
+ For information about refactoring your application by using AWS Blu Age, see the [AWS Mainframe Modernization documentation](https://docs.aws.amazon.com/m2/latest/userguide/refactoring-m2.html).
+ To understand how OAuth 2.0 works, see the [OAuth 2.0 website](https://oauth.net/2/).
+ For an overview of the Microsoft Authentication Library (MSAL), see the [Microsoft Entra documentation](https://learn.microsoft.com/en-us/azure/active-directory/develop/msal-overview).
+ For information about user profiles on an AS/400 system, see the [IBM i (AS400) tutorial](https://www.go4as400.com/subsystem-jobs-user-profile-in-as400/jobs.aspx?cid=14).
+ For the OAuth 2.0 and OpenID Connect (OIDC) authentication flow in the Microsoft identity platform, see the [Microsoft Entra documentation](https://learn.microsoft.com/en-us/entra/identity-platform/v2-protocols).
