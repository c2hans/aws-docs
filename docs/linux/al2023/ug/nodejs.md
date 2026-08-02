---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/nodejs.html
---

# Node.js in AL2023
<a name="nodejs"></a>

 [https://nodejs.org/](https://nodejs.org/) in AL2023 is represented by versions 20, 22 and 24. Amazon Linux follows the upstream [support schedule](https://github.com/nodejs/Release) and a support status of any Node.js version can always be checked on the [Package support status page](https://docs.aws.amazon.com/linux/al2023/release-notes/support-info-by-package.html). All supported Node.js versions are namespaced and can be installed on the same system simultaneously. Namespacing ensures that each Node.js installation is unique within the file system. This is achieved by renaming key directories and files based on the runtime version. The actual executable names will look like *node-{MAJOR\_VERSION}* or *npm-{MAJOR\_VERSION}*. However, only one Node.js version can be active at a time. This active version provides the default directories and file names, such as *node*, *npm* or */usr/lib/node\_modules*, pointing them to the currently active runtime.

 This is achieved using the capabilities of the *alternatives* tool. It is important to remember that the default executable names are virtual and can change at any time when pointing to a different installed Node.js version. This flexibility enables software that uses *node* in the shebang to select the desired version when invoked. However, when a specific version of Node.js is required, persistence of the version can be achieved by calling the namespaced executable (e.g., *node-20* or *node-22*), which will always use the specified version of the runtime. Additionally, the namespaced executables of the *npm* tool, such as npm-20 or npm-22, are always associated with the corresponding Node.js version, regardless of the currently active runtime.

 Node.js is distributed as several namespaced packages which begin with "`nodejs{MAJOR_VERSION}`". These packages provide *node*, a compatible version of the *npm* tool, documentation, libraries, and more. For example, *node* and *npm* of the Node.js 22 are provided by the `nodejs22` and `nodejs22-npm` packages, respectively.

 The *alternatives* tool provides a single command for switching between Node.js versions. By default, *alternatives* is configured to be in auto mode, which uses priorities to determine the currently active Node.js version. However, you can activate any installed version at any time. Currently, all supported versions of Node.js have equal priority, meaning the first installed version will be activated automatically.

**Some useful examples of using *alternatives***

1. Check what *alternatives* is configured for

   ```
   alternatives --list
   ```

1. Check *node*'s current configuration

   ```
   alternatives --display node
   ```

1. Interactively change the Node.js version

   ```
   alternatives --config node
   ```

1. Switch to manual mode and select a specific version

   ```
   alternatives --set node /usr/bin/node-{MAJOR_VERSION}
   ```

1. Switch back to auto version selection mode

   ```
   alternatives --auto node
   ```
