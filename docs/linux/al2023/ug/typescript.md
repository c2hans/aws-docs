---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/typescript.html
---

# TypeScript in AL2023
<a name="typescript"></a>

**Note**
 This document provides the essential information on TypeScript and its Node.js-based execution environment. It also covers a typical development workflow and explains how TypeScript is packaged in AL2023 to deliver a consistent and reproducible development environment.

 [https://www.typescriptlang.org/](https://www.typescriptlang.org/) (TS) is a programming language based on JavaScript (JS) that offers all JS’s features, and also [extends it with a type system](https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html). In a typical scenario, programs written in TS are translated into the JS code first, and then executed as any other regular JS program by Node.js. In TS’s specific terminology, this translation process is called [“compilation” and is performed by a “compiler”](https://www.typescriptlang.org/docs/handbook/typescript-tooling-in-5-minutes.html), called *tsc*. The *tsc* compiler itself is written in JS, thus to run, it also needs a JS runtime environment, such as Node.js. Unlike some other JS runtime environments, Node.js currently has only experimental and lightweight TS support. A full TS support, including type checking, still requires using third-party packages, such as the [typescript](https://www.npmjs.com/package/typescript). The expected way to get *tsc* (the TS compiler) for the Node.js runtime environment is to install the typescript node module. This can be done using one of the package managers, typically *npm*. There are two ways to install the TS compiler using *npm*: globally and in a project. [The officially recommended method is to install](https://www.typescriptlang.org/download/) the TS compiler on a per-project basis, which ensures long-term consistency and reproducibility for projects. However, installing the TS compiler globally might still be useful, because it provides the same version for the entire host and its JS runtime, and thus for projects that don’t have a TS compiler installed locally. This is precisely how RPM packages available on Amazon Linux, such as `nodejs20-typescript` or `nodejs22-typescript`, install a TS compiler: globally at the system level, and separately for each supported Node.js version.

 The *tsc* doesn’t directly depend on any Node.js version. The compiler expects a certain level of the runtime features, which are defined in a special file (*tsconfig.json*) via options such as [target](https://www.typescriptlang.org/tsconfig/#target) and [lib](https://www.typescriptlang.org/tsconfig/#lib). The values of these options represent a version of the [ECMAScript](https://en.wikipedia.org/wiki/ECMAScript_version_history) (ES) standard, which may (or may not) be supported by the JS runtime environment. Different versions of Node.js support different versions of ES standard. The more recent the version of Node.js, the higher and more complete the ES standard version supported. If *tsconfig.json* does not exist in the root directory of a project, then the default set of configuration options will be used. The compatibility table with the different versions of Node.js and the supported features of various ES standard versions is available at [node.green](https://node.green/). The *tsc* has more than 100 different options, which can be defined in the *tsconfig.json*. Configuration chaining is also supported, when some configuration options are defined in another file and then included in the main file. This approach allows one to install a [Base TS Config](https://github.com/tsconfig/bases) compatible with a certain version of Node.js, and then extend it with project-specific options. Fortunately, the Base TS Configs for Node.js are available as node modules which can be installed in a project folder using *npm*. Here is the config’s source code for Node.js version [18](https://github.com/tsconfig/bases/blob/main/bases/node18.json), [20](https://github.com/tsconfig/bases/blob/main/bases/node20.json), and [22](https://github.com/tsconfig/bases/blob/main/bases/node22.json).

 The Node.js based runtime design has a certain weakness: it supports only one version of the runtime on a host, and requires reproducibility and consistency of all dependencies at the project level. This led to the following common approach of using TypeScript: the TS compiler, TS base config for the current Node.js version, and all software dependencies are installed locally, inside a project. Although globally installed node modules are expected to be CLI tools only, such as *npm*, *tsc*, which is also a CLI tool, is rarely installed globally. Thankfully, global (system wide) and local (within a project) installations of *tsc* can co-exist with no issues and can also be different versions which are used independently. Note that a locally installed *tsc* should be executed using the *npx* tool, which is installed together with *npm*. Thus, even with a system TS compiler, users have the opportunity to choose versions of the runtime's components, such as Node.js (by switching the active version via alternatives), a TS compiler (by either installing it locally, or, globally and also switching the active version via alternatives), and configuring it for the specific needs.

 Amazon Linux packages a TS compiler in the same way as other globally installed node modules, such as *npm*, on a per Node.js version basic. Packages and binaries are namespaced and contain the major version of Node.js as part of their names. The default executable name of the compiler, *tsc*, is managed at runtime by the alternatives tool and point the currently active version of Node.js for which it was insatalled and will be executed by. This selection doesn't depened on the current Node.js runtime version. It is possible to have *node* executable pointing to Node.js 20 and *tsc* configured to be interpreted by the Node.js 22. It is also possible to use the namespaced names of a TS compiler, e.g. *tsc-{MAJOR\_VERSION}* independently to what the default *tsc* name is configured for.

**Some useful commands for managing the active version of a TS compiler**

1. Check what *alternatives* is configured for

   ```
   alternatives --list
   ```

1. Check *tsc*'s current configuration

   ```
   alternatives --display tsc
   ```

1. Interactively change the tsc version

   ```
   alternatives --config tsc
   ```

1. Switch to manual mode and select a specific version

   ```
   alternatives --set tsc /usr/bin/tsc-{MAJOR_VERSION}
   ```

1. Switch back to auto version selection mode

   ```
   alternatives --auto tsc
   ```

 An example of installing and using several versions of Node and a TS compiler on the same system:

```
# Check the AL2023 release
$ cat /etc/amazon-linux-release
Amazon Linux release 2023.9.20250929 (Amazon Linux)

# Install a TypeScript compiler for Node.js 20 and 22
# Node.js 20 and 22 will be installed automatically
$ sudo dnf install -qy nodejs20-typescript nodejs22-typescript

# Check what was installed
$ rpm -q nodejs20 nodejs20-typescript nodejs22 nodejs22-typescript
nodejs20-20.19.5-1.amzn2023.0.1.x86_64
nodejs20-typescript-5.9.2-1.amzn2023.0.1.noarch
nodejs22-22.19.0-1.amzn2023.0.1.x86_64
nodejs22-typescript-5.9.2-1.amzn2023.0.1.noarch

# Check the active version of Node.js - it is version 20
$ alternatives --display node
node - status is auto.
 link currently points to /usr/bin/node-20
/usr/bin/node-20 - priority 100
 slave npmrc: /usr/lib/nodejs20/lib/node_modules/npm/npmrc
 slave npm: /usr/bin/npm-20
 slave npx: /usr/bin/npx-20
 slave node_modules: /usr/lib/nodejs20/lib/node_modules
/usr/bin/node-22 - priority 100
 slave npmrc: /usr/lib/nodejs22/lib/node_modules/npm/npmrc
 slave npm: /usr/bin/npm-22
 slave npx: /usr/bin/npx-22
 slave node_modules: /usr/lib/nodejs22/lib/node_modules
Current 'best' version is /usr/bin/node-20.

# Check the active JS runtime version for TypeScript
# Currently, the tsc compiler will be executed by Node.js 22
$ alternatives --display tsc
tsc - status is auto.
 link currently points to /usr/bin/tsc-22
/usr/bin/tsc-22 - priority 100
 slave tsserver: /usr/bin/tsserver-22
/usr/bin/tsc-20 - priority 100
 slave tsserver: /usr/bin/tsserver-20
Current 'best' version is /usr/bin/tsc-22.

# Check versions printed by executables
$ node -v
v20.19.5

$ tsc -v
Version 5.9.2

# while the node is 20, tsc is executed by node 22 anyway
$ head -1 /usr/bin/tsc
#!/usr/bin/node-22

# However, instead of default executable names, e.g. node or tsc,
# we can use namespaced names to target any installed version
$ node-20 -v
v20.19.5

$ node-22 -v
v22.19.0

$ tsc-20 -v
Version 5.9.2

$ tsc-22 -v
Version 5.9.2

$ head -1 /usr/bin/tsc-20
#!/usr/bin/node-20

$ head -1 /usr/bin/tsc-22
#!/usr/bin/node-22
```
