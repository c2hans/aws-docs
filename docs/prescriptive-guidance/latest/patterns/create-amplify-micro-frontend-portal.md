---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-amplify-micro-frontend-portal.html
---

# Create a portal for micro-frontends by using AWS Amplify, Angular, and Module Federation
<a name="create-amplify-micro-frontend-portal"></a>

*Milena Godau and Pedro Garcia, Amazon Web Services*

## Summary
<a name="create-amplify-micro-frontend-portal-summary"></a>

A micro-frontend architecture enables multiple teams to work on different parts of a frontend application independently. Each team can develop, build, and deploy a fragment of the frontend without interfering with other parts of the application. From the end user's perspective, it appears to be a single, cohesive application. However, they are interacting with several independent applications that are published by different teams.

This document describes how to create a micro-frontend architecture by using [AWS Amplify](https://docs.amplify.aws/gen1/angular/), the [Angular](https://angular.dev/overview) frontend framework, and [Module Federation](https://webpack.js.org/concepts/module-federation/). In this pattern, the micro-frontends are combined on the client side by a shell (or *parent*) application. The shell application acts as a container that retrieves, displays, and integrates the micro-frontends. The shell application handles the global routing, which loads different micro-frontends. The [@angular-architects/module-federation](https://www.npmjs.com/package/@angular-architects/module-federation) plugin integrates Module Federation with Angular. You deploy the shell application and micro-frontends by using AWS Amplify. End users access the application through a web-based portal.

The portal is split vertically. This means that the micro-frontends are entire views or groups of views, instead of parts of the same view. Therefore the shell application loads only one micro-frontend at a time.

The micro-frontends are implemented as remote modules. The shell application lazily loads these remote modules, which defers the micro-frontend initialization until it is required. This approach optimizes application performance by loading only the necessary modules. This reduces the initial load time and improves the overall user experience. Additionally, you share common dependencies across modules through the webpack configuration file (**webpack.config.js**). This practice promotes code reuse, reduces duplication, and streamlines the bundling process.

## Prerequisites and limitations
<a name="create-amplify-micro-frontend-portal-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ Node.js and npm, [installed](https://nodejs.org/en/download/)
+ Amplify CLI, [installed](https://docs.amplify.aws/gen1/angular/tools/cli/)
+ Angular CLI, [installed](https://angular.io/cli)
+ [Permissions](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsamplify.html) to use AWS Amplify
+ Familiarity with Angular

**Product versions**
+ Angular CLI version 13.1.2 or later
+ @angular-architects/module-federation version 14.0.1 or later
+ webpack version 5.4.0 or later
+ AWS Amplify Gen 1

**Limitations**

A micro-frontend architecture is a powerful approach for building scalable and resilient web applications. However, it's crucial to understand the following potential challenges before adopting this approach:
+ **Integration** – One of the key challenges is the potential increase in complexity compared to monolithic frontends. Orchestrating multiple micro-frontends, handling communication between them, and managing shared dependencies can be more intricate. Additionally, there may be a performance overhead associated with communication between the micro-frontends. This communication can increase latency and reduce performance. This needs to be addressed through efficient messaging mechanisms and data-sharing strategies.
+ **Code duplication** – Because each micro-frontend is developed independently, there is a risk of duplicating code for common functionality or shared libraries. This can increase the overall application size and introduce maintenance challenges.
+ **Coordination and management** – Coordinating the development and deployment processes across multiple micro-frontends can be challenging. Ensuring consistent versioning, managing dependencies, and maintaining compatibility between components becomes more critical in a distributed architecture. Establishing clear governance, guidelines, and automated testing and deployment pipelines is essential for seamless collaboration and delivery.
+ **Testing** – Testing micro-frontend architectures can be more complex than testing monolithic frontends. It requires additional effort and specialized testing strategies to perform cross-component integration testing and end-to-end testing, and to validate consistent user experiences across multiple micro-frontends.

Before committing to the micro-frontend approach, we recommend that you review [Understanding and implementing micro-frontends on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/introduction.html).

## Architecture
<a name="create-amplify-micro-frontend-portal-architecture"></a>

In a micro-frontend architecture, each team develops and deploys features independently. The following image shows how multiple DevOps teams work together. The portal team develops the shell application. The shell application acts as a container. It retrieves, displays, and integrates the micro-frontend applications that are published by other DevOps teams. You use AWS Amplify to publish the shell application and micro-frontend applications.

![Publishing multiple micro-frontends to a shell app that the user accesses through a web portal.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/ddf82a69-bf1b-4ad1-8e60-3dd375699936/images/cf045bf1-11ea-46d9-93cb-3c603122450d.png)

The architecture diagram shows the following workflow:

1. The portal team develops and maintains the shell application. The shell application orchestrates the integration and rendering of the micro-frontends in order to compose the overall portal.

1. Teams A and B develop and maintain one or more micro-frontends or features that are integrated into the portal. Each team can work independently on their respective micro-frontends.

1. The end user authenticates by using Amazon Cognito.

1. The end user accesses the portal, and the shell application is loaded. As the user navigates, the shell application deals with the routing and retrieves the requested micro-frontend, loading its bundle.

## Tools
<a name="create-amplify-micro-frontend-portal-tools"></a>

**AWS services**
+ [AWS Amplify](https://docs.amplify.aws/angular/start/) is a set of purpose-built tools and features that helps frontend web and mobile developers quickly build full-stack applications on AWS. In this pattern, you use the Amplify CLI to deploy the Amplify micro-frontend applications.
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open source tool that helps you interact with AWS services through commands in your command-line shell.

**Other tools**
+ [@angular-architects/module-federation](https://github.com/angular-architects/module-federation-plugin) is a plugin that integrates Angular with Module Federation.
+ [Angular](https://angular.dev/overview) is an open source web application framework for building modern, scalable, and testable single-page applications. It follows a modular and component-based architecture that promotes code reuse and maintenance.
+ [Node.js](https://nodejs.org/en/docs/) is an event-driven JavaScript runtime environment designed that is for building scalable network applications.
+ [npm](https://docs.npmjs.com/about-npm) is a software registry that runs in a Node.js environment and is used to share or borrow packages and manage deployment of private packages.
+ [Webpack Module Federation](https://webpack.js.org/concepts/module-federation/) helps you load code that is independently compiled and deployed, such as micro-frontends or plugins, into an application.

**Code repository**

The code for this pattern is available in the [Micro-frontend portal using Angular and Module Federation](https://github.com/aws-samples/angular-module-federation-mfe) GitHub repository. This repository contains the following two folders:
+ `shell-app` contains the code for the shell application.
+ `feature1-app` contains a sample micro-frontend. The shell application fetches this micro-frontend and displays it as a page within the portal application.

## Best practices
<a name="create-amplify-micro-frontend-portal-best-practices"></a>

Micro-frontend architectures offer numerous advantages, but they also introduce complexity. The following are some best practices for smooth development, high-quality code, and a great user experience:
+ **Planning and communication** – To streamline collaboration, invest in upfront planning, design, and clear communication channels.
+ **Design consistency** – Enforce a consistent visual style across micro-frontends by using design systems, style guides, and component libraries. This provides a cohesive user experience and accelerates development.
+ **Dependency management** – Because micro-frontends evolve independently, adopt standardized contracts and versioning strategies to manage dependencies effectively and prevent compatibility issues.
+ **Micro-frontend architecture** – To enable independent development and deployment, each micro-frontend should have a clear and well-defined responsibility for an encapsulated functionality.
+ **Integration and communication** – To facilitate smooth integration and minimize conflicts, define clear contracts and communication protocols between micro-frontends, including APIs, events, and shared data models.
+ **Testing and quality assurance** – Implement test automation and continuous integration pipelines for micro-frontends. This improves the overall quality, reduces manual testing effort, and validates functionality between micro-frontend interactions.
+ **Performance optimization** –** **Continuously monitor performance metrics and track dependencies between micro-frontends. This helps you identify bottlenecks and maintain optimal application performance. Use performance monitoring and dependency analysis tools for this purpose.
+ **Developer experience** – Focus on the developer experience by providing clear documentation, tooling, and examples. This helps you streamline development and onboard new team members.

## Epics
<a name="create-amplify-micro-frontend-portal-epics"></a>

### Create the shell application
<a name="create-the-shell-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the shell application. | 1. In the Angular CLI, enter the following command:<pre>ng new shell --routing</pre><br />2. Enter the following command to navigate to the project folder:<pre>cd shell</pre>The folder and project structure for the shell and micro-frontend applications can be totally independent. They can be handled as independent Angular applications. | App developer |
| Install the plugin. | In the Angular CLI, enter the following command to install the [@angular-architects/module-federation](https://www.npmjs.com/package/@angular-architects/module-federation) plugin:<pre>ng add @angular-architects/module-federation --project shell --port 4200</pre> | App developer |
| Add the micro-frontend URL as an environment variable. | 1. Open the **environment.ts** file.<br />2. Add `mfe1URL: 'http://localhost:5000'` to the `environment` object:<pre>export const environment = {<br />  production: false,<br />  mfe1URL: 'http://localhost:5000',<br />};</pre><br />3. Save and close the **environment.ts** file. | App developer |
| Define routing. | 1. Open the **app-routing.module.ts** file.<br />2. In the Angular CLI, enter the following command to import the `loadRemoteModule` module from the @angular-architects/module-federation plugin:<pre>import { loadRemoteModule } from '@angular-architects/module-federation';</pre><br />3. Set the default route as the following:<pre>{<br />    path: '',<br />    pathMatch: 'full',<br />    redirectTo: 'mfe1'<br />  },</pre><br />4. Set the route for the micro-frontend:<pre>{<br />    path: 'mfe1',<br />    loadChildren: () => loadRemoteModule({<br />        type: 'module',<br />        remoteEntry: `${environment.mfe1URL}/remoteEntry.js`,<br />        exposedModule: './Module'<br />      })<br />      .then(m => m.Mfe1Module)<br />  },</pre><br />5. Save and close the **app-routing.module.ts** file. | App developer |
| Declare the `mfe1` module. | 1. In the `src` folder, create a new file named **decl.d.ts**.<br />2. Open the **decl.d.ts** file.<br />3. Add the following to the file:<pre>declare module 'mfe1/Module';</pre><br />4. Save and close the **decl.d.ts** file. | App developer |
| Prepare preloading for the micro-frontend. | Preloading the micro-frontend helps the webpack properly negotiate the shared libraries and packages.1. Open the** main.ts **file.<br />2. Replace the content with the following:<pre>import { loadRemoteEntry } from '@angular-architects/module-federation';<br /> <br />Promise.all([<br />    loadRemoteEntry(`${environment.mfe1URL}/remoteEntry.js`, 'mfe1'),<br />])<br />.catch(err => console.error('Error loading remote entries', err))<br />.then(() => import('./bootstrap'))<br />.catch(err => console.error(err));</pre><br />3. Save and close the **main.ts** file. | App developer |
| Adjust the HTML content. | 1. Open the **app.component.html** file.<br />2. Replace the content with the following:<pre><h1>Shell application is running!</h1><br /><router-outlet></router-outlet></pre><br />3. Save and close the** app.component.html** file. | App developer |

### Create the micro-frontend application
<a name="create-the-micro-frontend-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the micro-frontend. | 1. In the Angular CLI, enter the following command:<pre>ng new mfe1 --routing</pre><br />2. Enter the following command to navigate to the project folder:<pre>cd mfe1</pre> | App developer |
| Install the plugin. | Enter the following command to install the @angular-architects/module-federation plugin:<pre>ng add @angular-architects/module-federation --project mfe1 --port 5000</pre> | App developer |
| Create a module and component. | Enter the following commands to create a module and component and export them as the remote entry module:<pre>ng g module mfe1 --routing<br />ng g c mfe1</pre> | App developer |
| Set the default routing path. | 1. Open the **mfe-routing.module.ts** file.<br />2. Set the default route as the following:<pre>{<br />    path: '',<br />    component: Mfe1Component<br />  },</pre><br />3. Save and close the **mfe-routing.module.ts** file. | App developer |
| Add the `mfe1` route. | 1. Open the** app-routing.module.ts** file.<br />2. Set the default route as the following:<pre>{<br />    path: '',<br />    pathMatch: 'full',<br />    redirectTo: 'mfe1'<br />  },</pre><br />3. Add the following `mfe1` route:<pre>{<br />    path: 'mfe1',<br />    loadChildren: () => <br />      import('./mfe1/mfe1.module').then((m) => m.Mfe1Module),<br />  },</pre><br />4. Save and close the **app-routing.module.ts** file. | App developer |
| Edit the **webpack.config.js** file. | 1. Open the **webpack.config.js** file.<br />2. Edit the `For remotes` section to match the following:<pre>// For remotes (please adjust)<br />    name: "mfe1",<br />    filename: "remoteEntry.js",<br />    exposes: {<br />        './Module': './src/app/mfe1/mfe1.module.ts',<br />    },</pre><br />3. In the `shared` section, add any dependencies that the `mfe1` application shares with the shell application:<pre>shared: share({<br />        "@angular/core": { singleton: true, strictVersion: true, requiredVersion: 'auto' }, <br />        "@angular/common": { singleton: true, strictVersion: true, requiredVersion: 'auto' }, <br />        "@angular/common/http": { singleton: true, strictVersion: true, requiredVersion: 'auto' }, <br />        "@angular/router": { singleton: true, strictVersion: true, requiredVersion: 'auto' },<br />    <br />        ...sharedMappings.getDescriptors()<br />    })</pre><br />4. Save and close the** webpack.config.js** file. | App developer |
| Adjust the HTML content. | 1. Open the **app.component.html** file.<br />2. Replace the contents with the following:<pre><router-outlet></router-outlet></pre><br />3. Save and close the** app.component.html** file. | App developer |

### Run the applications locally
<a name="run-the-applications-locally"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Run the `mfe1` application. | 1. Enter the following command to start the `mfe1` application:<pre>npm start</pre><br />2. In a web browser, access `http://localhost:5000`.<br />3. Verify that the micro-frontend can be run standalone. The `mfe1` application should properly render without any errors. | App developer |
| Run the shell application. | 1. Enter the following command to start the shell application:<pre>npm start</pre><br />2. In a web browser, access `http://localhost:4200/mfe1`.<br />3. Verify that the `mfe1` micro-frontend is embedded in the shell application. The portal application should properly render without any errors, and the `mfe1` application should be embedded within it. | App developer |

### Refactor the shell application to handle a micro-frontend loading error
<a name="refactor-the-shell-application-to-handle-a-micro-frontend-loading-error"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a module and component. | In the root folder of the shell application, enter the following commands to create a module and component for an error page:<pre>ng g module error-page --routing<br />ng g c error-page</pre> | App developer |
| Adjust the HTML content. | 1. Open the **error-page.component.html** file.<br />2. Replace the contents with the following:<pre><p>Sorry, this page is not available.</p></pre><br />3. Save and close the **error-page.component.html** file. | App developer |
| Set the default routing path. | 1. Open the **error-page-routing.module.ts** file.<br />2. Set the default route as the following:<pre>{<br />    path: '',<br />    component: ErrorPageComponent<br />  },</pre><br />3. Save and close the **error-page-routing.module.ts** file. | App developer |
| Create a function to load micro-frontends. | 1. Open the **app-routing.module.ts** file.<br />2. Create the following function:<pre>function loadMFE(url: string) {<br />    return loadRemoteModule({<br />        type: 'module',<br />        remoteEntry: `${url}/remoteEntry.js`,<br />        exposedModule: './Module'<br />    })<br />    .then(m => m.Mfe1Module)<br />    .catch(<br />        () => import('./error-page/error-page.module').then(m => m.ErrorPageModule)<br />    );<br />}</pre><br />3. Modify the `mfe1` route to be the following:<pre>{<br />    path: 'mfe1',<br />    loadChildren: () => loadMFE(environment.mfe1URL)<br />},</pre><br />4. Save and close the** app-routing.module.ts** file. | App developer |
| Test the error handling. | 1. If it is not already running, enter the following command to start the shell application:<pre>npm start</pre><br />2. In a web browser, access `http://localhost:4200/mfe1`.<br />3. Verify that the error page is rendered. You should see the following text:<pre>Sorry, this page is not available.</pre> | App developer |

### Deploy the applications by using AWS Amplify
<a name="deploy-the-applications-by-using-amplifylong"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the micro-frontend. | 1. In the Amplify CLI, navigate to the root folder of the micro-frontend application.<br />2. Enter the following command to initialize Amplify:<pre>amplify init</pre><br />3. When you are prompted to enter a name for your Amplify project, press **Enter**. This re-uses the name from the **package.json** file.<br />4. When you are prompted to initialize the project with the above configuration, enter `Yes`.<br />5. When you are prompted to select an authentication method, choose `AWS Profile`.<br />6. Select the profile you want to use.<br />7. Wait for Amplify to initialize the project. When this process is complete, you receive a confirmation message in the terminal.<br />8. Enter the following command to add an Amplify hosting category to the micro-frontend:<pre>amplify add hosting</pre><br />9. When you are prompted to select the plugin module, choose `Hosting with Amplify Console`.<br />10. When you are prompted to choose a type, choose `Manual deployment`.<br />11. Install the project npm dependencies by entering the following command:<pre>npm install</pre><br />12. Publish the application to the Amplify console by entering the following command:<pre>amplify publish -y</pre><br />When publishing is complete, Amplify returns the URL of the micro-frontend.<br />13. Copy the URL. You need this value to update the shell application. | App developer, AWS DevOps |
| Deploy the shell application. | 1. In the **src/app/environments** folder, open the** environments.prod.ts** file.<br />2. Replace the `mfe1URL` value with the URL of the deployed micro-frontend:<pre>export const environment = {  <br />   production: true, <br />   mfe1URL: 'https://<env>.<Amplify-app-ID>.amplifyapp.com'<br /> };</pre><br />3. Save and close the** environments.prod.ts** file.<br />4. In the Amplify CLI, navigate to the root folder of the shell application.<br />5. Enter the following command to initialize Amplify:<pre>amplify init</pre><br />6. When you are prompted to enter a name for your Amplify project, press **Enter**. This re-uses the name from the **package.json** file.<br />7. When you are prompted to initialize the project with the above configuration, enter `Yes`.<br />8. When you are prompted to select an authentication method, choose `AWS Profile`.<br />9. Select the profile you want to use.<br />10. Wait for Amplify to initialize the project. When this process is complete, you receive a confirmation message in the terminal.<br />11. Add an Amplify hosting category to the shell application:<pre>amplify add hosting</pre><br />12. When you are prompted to select the plugin module, choose `Hosting with Amplify Console`.<br />13. When you are prompted to choose a type, choose `Manual deployment`.<br />14. Install project npm dependencies by entering the following command:<pre>npm install</pre><br />15. Publish the shell application to the Amplify console by entering the following command:<pre>amplify publish -y</pre><br />When publishing is complete, Amplify returns the URL of the deployed shell application.<br />16. Make note of the URL for the shell application. | App developer, App owner |
| Enable CORS. | Because the shell and micro-frontend applications are hosted independently on different domains, you must enable cross-origin resource sharing (CORS) on the micro-frontend. This allows the shell application to load the content from a different origin. To enable CORS, you add custom headers.1. In the Amplify CLI, navigate to the root folder of the micro-frontend.<br />2. Enter the following command:<pre>amplify configure hosting</pre><br />3. When you are prompted to configure custom settings, enter `Y`.<br />4. Sign in to the AWS Management Console, and then open the [Amplify console](https://console.aws.amazon.com/amplify/).<br />5. Choose the micro-frontend.<br />6. In the navigation pane, choose **Hosting**, and then choose **Custom headers**.<br />7. Choose **Edit**.<br />8. In the **Edit custom headers** window, enter the following:<pre>customHeaders:<br />  - pattern: '*.js'<br />    headers:<br />      - key: Access-Control-Allow-Origin<br />        value: '*'<br />      - key: Access-Control-Allow-Methods<br />        value: 'GET, OPTIONS'<br />      - key: Access-Control-Allow-Headers<br />        value: '*'</pre><br />9. Choose **Save**.<br />10. Redeploy the micro-frontend to apply the new custom headers. | App developer, AWS DevOps |
| Create a rewrite rule on the shell application. | The Angular shell application is configured to use HTML5 routing. If the user performs a hard refresh, Amplify tries to load a page from the current URL. This generates a 403 error. To avoid this, you add a rewrite rule in the Amplify console.<br />To create the rewrite rule, follow these steps:1. In the Amplify CLI, navigate to the root folder of the shell application.<br />2. Enter the following command:<pre>amplify configure hosting</pre><br />3. When you are prompted to configure custom settings, enter `Y`.<br />4. Open the [Amplify console](https://console.aws.amazon.com/amplify/).<br />5. Choose the shell application.<br />6. In the navigation pane, choose **Hosting**, and then choose **Rewrites and redirects**.<br />7. On the **Rewrites and redirects** page, choose **Manage redirects**.<br />8. Choose **Open text editor**.<br />9. In the JSON editor, enter the following redirect:<pre>[<br />    {<br />        "source": "/<*>",<br />        "target": "/index.html",<br />        "status": "404-200",<br />        "condition": null<br />    }<br />]</pre><br />10. Choose **Save**. | App developer, AWS DevOps |
| Test the web portal. | 1. In a web browser, enter the URL of the deployed shell application.<br />2. Verify that the shell application and the micro-frontend load properly. | App developer |

### Clean up resources
<a name="clean-up-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete the applications. | If you no longer need the shell and micro-frontend applications, delete them. This helps prevent charges for resources that you aren't using.1. Sign in to the AWS Management Console, and then open the [Amplify console](https://console.aws.amazon.com/amplify/).<br />2. Choose the micro-frontend.<br />3. In the navigation pane, choose **App settings**, and then choose **General settings**.<br />4. Choose **Delete app**.<br />5. In the confirmation window, enter `delete`, and then choose **Delete app**.<br />6. Repeat these steps to delete the shell application. | General AWS |

## Troubleshooting
<a name="create-amplify-micro-frontend-portal-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| No AWS profile available when running the `amplify init` command | If you don't have an AWS profile configured, you can still proceed with the `amplify init` command. However, you need to select the `AWS access keys` option when you're prompted for the authentication method. Have your AWS access key and secret key available.<br />Alternatively, you can configure a named profile for the AWS CLI. For instructions, see [Configuration and credential file settings](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) in the AWS CLI documentation. |
| Error loading remote entries | If you encounter an error when loading the remote entries in the **main.ts** file of the shell application, make sure that the `environment.mfe1URL` variable is set correctly. The value of this variable should be the URL of the micro-frontend. |
| 404 error when accessing the micro-frontend | If you get a 404 error when trying to access the local micro-frontend, such as at `http://localhost:4200/mfe1`, check the following:+ For the shell application, make sure that the routing configuration in the **app-routing.module.ts** file is set up correctly, and make sure that the `loadRemoteModule` function is properly calling the micro-frontend.<br />+ For the micro-frontend, verify that the **webpack.config.js** file has the correct `exposes` configuration, and make sure that the **remoteEntry.js** file is being generated correctly. |

## Additional information
<a name="create-amplify-micro-frontend-portal-additional"></a>

**AWS documentation**
+ [Understanding and implementing micro-frontends on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/micro-frontends-aws/introduction.html) (AWS Prescriptive Guidance)
+ [Amplify CLI](https://docs.amplify.aws/gen1/angular/tools/cli/) (Amplify documentation)
+ [Amplify Hosting](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html) (Amplify documentation)

**Other references **
+ [Module Federation](https://webpack.js.org/concepts/module-federation/)
+ [Node.js](https://nodejs.org/en/)
+ [Angular](https://angular.io/)
+ [@angular-architects/module-federation](https://www.npmjs.com/package/@angular-architects/module-federation)
