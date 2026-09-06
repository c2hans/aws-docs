---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/typescript.html
---

# TypeScript in AL2027
<a name="typescript"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

**Note**
 This topic provides the essential information about TypeScript and its Node.js based execution environment. It also covers a typical development workflow. It explains how AL2027 packages TypeScript to deliver a consistent and reproducible development environment.

 TypeScript (TS) is a programming language based on JavaScript (JS). It offers all JS features and extends them with a type system. For more information, see the [TypeScript website](https://www.typescriptlang.org/) and [the TypeScript type system](https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html) on the TypeScript website.

 In a typical scenario, a program written in TS is first translated into JS code. Node.js then runs the result as any other regular JS program. TS terminology calls this translation process *compilation*, and calls the tool that performs it a *compiler*. The TS compiler is named *tsc*. For more information, see [compiling TypeScript](https://www.typescriptlang.org/docs/handbook/typescript-tooling-in-5-minutes.html) on the TypeScript website.

 The *tsc* compiler is itself written in JS. To run, it needs a JS runtime environment, such as Node.js. Unlike some other JS runtime environments, Node.js currently provides only experimental and lightweight TS support. Full TS support, including type checking, still requires a third-party package, such as [typescript](https://www.npmjs.com/package/typescript) on the npm website.

 To get *tsc* for the Node.js runtime environment, install the `typescript` node module. You can install it with one of the package managers, typically *npm*, either globally or in a project. The [officially recommended method](https://www.typescriptlang.org/download/) on the TypeScript website is to install the compiler for each project. This approach ensures long-term consistency and reproducibility for your projects.

 Installing the compiler globally can still be useful. A global installation provides the same version for the entire host and its JS runtime, including projects that don't have a compiler installed locally. Amazon Linux packages a compiler in exactly this way. Packages such as `nodejs24-typescript` install a compiler globally at the system level, separately for each supported Node.js version.

 The *tsc* compiler doesn't directly depend on any Node.js version. Instead, it expects a certain level of runtime features. You define these features in a special file (*tsconfig.json*) through options such as [target](https://www.typescriptlang.org/tsconfig/#target) and [lib](https://www.typescriptlang.org/tsconfig/#lib) on the TypeScript website. The values of these options represent a version of the ECMAScript (ES) standard, which the JS runtime environment might (or might not) support. For more information, see [ECMAScript version history](https://en.wikipedia.org/wiki/ECMAScript_version_history) on Wikipedia.

 Different versions of Node.js support different versions of the ES standard. The more recent the version of Node.js, the higher and more complete the supported ES standard version. If *tsconfig.json* does not exist in the root directory of a project, *tsc* uses the default set of configuration options. For a compatibility table of Node.js versions and the supported features of various ES standard versions, see [node.green](https://node.green/) on the node.green website.

 The *tsc* compiler has more than 100 different options that you can define in *tsconfig.json*. It also supports configuration chaining, where one file defines some configuration options and the main file then includes that file. With this approach, you can install a base configuration that is compatible with a certain version of Node.js, and then extend it with project-specific options. For more information, see [Base TS Config](https://github.com/tsconfig/bases) on the GitHub website.

 The base configurations for Node.js are available as node modules that you can install in a project folder using *npm*. For the source of the configuration for Node.js version 24, see [node24.json](https://github.com/tsconfig/bases/blob/main/bases/node24.json) on the GitHub website.

 The Node.js based runtime design has a certain weakness. It supports only one version of the runtime on a host, and it requires reproducibility and consistency of all dependencies at the project level. This constraint led to a common approach for using TypeScript. You install the compiler, the TS base configuration for the current Node.js version, and all software dependencies locally, inside a project.

 Globally installed node modules are expected to be CLI tools only, such as *npm*. Although *tsc* is also a CLI tool, users rarely install it globally. Global (system-wide) and local (within a project) installations of *tsc* can co-exist without issues. The two installations can also be different versions that you use independently. Run a locally installed *tsc* with the *npx* tool, which *npm* installs.

 Even with a system TS compiler, you can choose the versions of the runtime components. You can switch the active Node.js version with the *alternatives* tool. You can also select a compiler version, either by installing it locally, or by installing it globally and then switching the active version with *alternatives*.

 Amazon Linux packages a TS compiler in the same way as other globally installed node modules, such as *npm*, for each Node.js version. Amazon Linux namespaces packages and binaries, and includes the major version of Node.js in their names. The *alternatives* tool manages the default executable name of the compiler, *tsc*, at runtime. It points *tsc* to the Node.js version that the compiler was installed for and runs under. This selection doesn't depend on the current Node.js runtime version. You can also use the namespaced name of a compiler, for example *tsc-{MAJOR\_VERSION}*, regardless of what the default *tsc* name points to.

**Some useful commands for managing the active version of a TS compiler**

1. Check what *alternatives* is configured for

   ```
   alternatives --list
   ```

1. Check *tsc*'s current configuration

   ```
   alternatives --display tsc
   ```

1. Interactively change the *tsc* version

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
