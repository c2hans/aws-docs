---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/authenticate-react-app-users-cognito-amplify-ui.html
---

# Authenticate existing React application users by using Amazon Cognito and AWS Amplify UI
<a name="authenticate-react-app-users-cognito-amplify-ui"></a>

*Daniel Kozhemyako, Amazon Web Services*

## Summary
<a name="authenticate-react-app-users-cognito-amplify-ui-summary"></a>

This pattern shows how to add authentication capabilities to an existing frontend React application by using an AWS Amplify UI library and an Amazon Cognito user pool.

The pattern uses Amazon Cognito to provide authentication, authorization, and user management for the application. It also uses a component from [Amplify UI](https://ui.docs.amplify.aws/react/getting-started/introduction), an open-source library that extends the capabilities of AWS Amplify to user interface (UI) development. The [Authenticator UI](https://ui.docs.amplify.aws/react/connected-components/authenticator/advanced) component manages login sessions and runs the cloud-connected workflow that authenticates users through Amazon Cognito.

After you implement this pattern, users can sign in by using any of the following credentials:
+ User name and password
+ Social identity providers, such as Apple, Facebook, Google, and Amazon
+ Enterprise identity providers that are either SAML 2.0 compatible or OpenID Connect (OIDC) compatible

**Note**
To create a custom authentication UI component, you can run the Authenticator UI component in headless mode.

## Prerequisites and limitations
<a name="authenticate-react-app-users-cognito-amplify-ui-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ A React 18.2.0 or later web application
+ Node.js and npm 6.14.4 or later, [installed](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)

**Limitations**
+ This pattern applies to React web applications only.
+ This pattern uses a prebuilt Amplify UI component. The solution doesn’t cover the steps required to implement a custom UI component.

**Product versions**
+ Amplify UI 6.1.3 or later (Gen 1)
+ Amplify 6.0.16 or later (Gen 1)

## Architecture
<a name="authenticate-react-app-users-cognito-amplify-ui-architecture"></a>

**Target architecture**

The following diagram shows an architecture that uses Amazon Cognito to authenticate users for a React web application.

![Amazon Cognito authenticates users for a React web application.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/b2cea053-6931-4404-8aa8-c623ce2024ac/images/b7f69f20-a39d-4a78-8605-7dab73c59052.png)

## Tools
<a name="authenticate-react-app-users-cognito-amplify-ui-tools"></a>

**AWS services**
+ [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) provides authentication, authorization, and user management for web and mobile apps.

**Other tools**
+ [Amplify UI](https://ui.docs.amplify.aws/react/getting-started/introduction) is an open-source UI library that provides customizable components that you can connect to the cloud.
+ [Node.js](https://nodejs.org/en/docs/) is an event-driven JavaScript runtime environment designed for building scalable network applications.
+ [npm](https://docs.npmjs.com/about-npm) is a software registry that runs in a Node.js environment and is used to share or borrow packages and manage deployment of private packages.

## Best practices
<a name="authenticate-react-app-users-cognito-amplify-ui-best-practices"></a>

If you're building a new application, we recommend that you use Amplify Gen 2.

## Epics
<a name="authenticate-react-app-users-cognito-amplify-ui-epics"></a>

### Create an Amazon Cognito user pool
<a name="create-an-cog-user-pool"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a user pool. | [Create an Amazon Cognito user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/tutorial-create-user-pool.html). Configure the user pool’s sign-in options and security requirements to fit your use case. | App developer |
| Add an app client. | [Configure a user pool app client](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-client-apps.html). This client is required for your application to interact with the Amazon Cognito user pool. | App developer |

### Integrate your Amazon Cognito user pool with the Authenticator UI component
<a name="integrate-your-cog-user-pool-with-the-authenticator-ui-component"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install dependencies. | To install the `aws-amplify` and `@aws-amplify/ui-react` packages, run the following command from your application’s root directory:<pre>npm i @aws-amplify/ui-react aws-amplify</pre> | App developer |
| Configure the user pool. | Based on the following example, create an `aws-exports.js` file and save in the `src` folder. The file should include the following information:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/authenticate-react-app-users-cognito-amplify-ui.html)<pre>// replace the user pool region, id, and app client id details<br />const awsmobile = {<br />    "aws_project_region": "put_your_region_here",<br />    "aws_cognito_region": "put_your_region_here",<br />    "aws_user_pools_id": "put_your_user_pool_id_here",<br />    "aws_user_pools_web_client_id": "put_your_user_pool_app_id_here"<br />}<br /><br />export default awsmobile;</pre> | App developer |
| Import and configure the Amplify service. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/authenticate-react-app-users-cognito-amplify-ui.html) | App developer |
| Add the Authenticator UI component. | To display the `Authenticator` UI component, add the following lines of code to the application’s entry point file (`App.js`):<pre>import { Authenticator } from '@aws-amplify/ui-react';<br />import '@aws-amplify/ui-react/styles.css';</pre>The example code snippet imports the `Authenticator` UI component and the Amplify UI styles.css file, which is required when using the component’s prebuilt themes.<br />The `Authenticator` UI component provides two return values:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/authenticate-react-app-users-cognito-amplify-ui.html)<br />See the following example component:<pre>function App() {<br />    return (<br />        <Authenticator><br />            {({ signOut, user }) => (<br />                <div><br />                    <p>Welcome {user.username}</p><br />                    <button onClick={signOut}>Sign out</button><br />                </div><br />            )}<br />        </Authenticator><br />    );<br />}</pre>For an example `App.js` file, see the [Additional information](#authenticate-react-app-users-cognito-amplify-ui-additional) section of this pattern. | App developer |
| (Optional) Retrieve session information. | After a user is authenticated, you can retrieve data from the Amplify client about their session. For example, you can retrieve the JSON web token (JWT) from a user’s session so that you can authenticate the requests from their session to a backend API.<br />See the following example of a request header that includes a JWT:<pre>import { fetchAuthSession } from 'aws-amplify/auth';<br />(await fetchAuthSession()).tokens?.idToken?.toString();</pre> | App developer |

## Troubleshooting
<a name="authenticate-react-app-users-cognito-amplify-ui-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| New users can’t sign up for the application. | As follows, make sure that your Amazon Cognito user pool is configured to allow users to sign themselves up to be in the user pool:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/authenticate-react-app-users-cognito-amplify-ui.html) |
| Auth component stopped working after upgrading from v5 to v6. | The `Auth` category has moved to a functional approach and named parameters in Amplify v6. You must now import the functional APIs directly from the `aws-amplify/auth` path. For more information, see [Migrate from v5 to v6](https://docs.amplify.aws/gen1/react/build-a-backend/auth/auth-migration-guide/) in the Amplify documentation. |

## Related resources
<a name="authenticate-react-app-users-cognito-amplify-ui-resources"></a>
+ [Getting started with Amazon Cognito](https://aws.amazon.com/cognito/getting-started/) (AWS website)
+ [Create a new React app](https://reactjs.org/docs/create-a-new-react-app.html) (React documentation)
+ [What is Amazon Cognito?](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) (Amazon Cognito documentation)
+ [Amplify UI library](https://ui.docs.amplify.aws/) (Amplify documentation)

## Additional information
<a name="authenticate-react-app-users-cognito-amplify-ui-additional"></a>

The `App.js` file should contain the following code:

```
import './App.css';
import { Amplify } from 'aws-amplify';
import awsExports from './aws-exports';
import { fetchAuthSession } from 'aws-amplify/auth';
import { Authenticator } from '@aws-amplify/ui-react';
import '@aws-amplify/ui-react/styles.css';
Amplify.configure({ ...awsExports });
let token = (await fetchAuthSession()).tokens?.idToken?.toString();
function App() {
  return (
      <Authenticator>
        {({ signOut, user }) => (
            <div>
              <p>Welcome {user.username}</p>
                <p>Your token is: {token}</p>
              <button onClick={signOut}>Sign out</button>
            </div>
        )}
      </Authenticator>
  );
}

export default App;
```
