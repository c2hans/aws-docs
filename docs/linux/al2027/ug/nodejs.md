---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/nodejs.html
---

# Node.js in AL2027
<a name="nodejs"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

 AL2027 includes Node.js 24. For more information about the runtime, see the [Node.js website](https://nodejs.org/). Amazon Linux follows the upstream [Node.js support schedule](https://github.com/nodejs/Release) on the GitHub website. To check the support status of a specific Node.js version, see the [Package support information](https://docs.aws.amazon.com/linux/al2027/release-notes/support-information.html) page.

 Amazon Linux namespaces all supported Node.js versions so that you can install them on the same system at the same time. Namespacing makes each Node.js installation unique within the file system. To do this, Amazon Linux renames key directories and files based on the runtime version. The resulting executable names look like *node-{MAJOR\_VERSION}* or *npm-{MAJOR\_VERSION}*.

 Only one Node.js version can be active at a time. The active version provides the default directory and file names, such as *node*, *npm*, or */usr/lib/node\_modules*, and points them to the currently active runtime. The *alternatives* tool provides this capability.

 The default executable names are virtual and can change at any time to point to a different installed Node.js version. This flexibility lets software that uses *node* in the shebang select the desired version when invoked. When you need a specific version of Node.js, call the namespaced executable, for example *node-24*. A namespaced executable always uses the version of the runtime that its name specifies. The namespaced executables of the *npm* tool, such as *npm-24*, always use the corresponding Node.js version, regardless of the currently active runtime.

 Amazon Linux distributes Node.js as several namespaced packages that begin with `nodejs{MAJOR_VERSION}`. These packages provide *node*, a compatible version of the *npm* tool, documentation, libraries, and more. For example, the `nodejs24` and `nodejs24-npm` packages provide *node* and *npm* for Node.js 24.

 The *alternatives* tool provides a single command for switching between Node.js versions. By default, *alternatives* runs in auto mode and uses priorities to determine the active Node.js version. However, you can activate any installed version at any time. All supported versions of Node.js currently have equal priority, so Amazon Linux activates the first version that you install.

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
