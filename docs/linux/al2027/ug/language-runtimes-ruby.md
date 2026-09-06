---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/language-runtimes-ruby.html
---

# Ruby in AL2027
<a name="language-runtimes-ruby"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

 AL2027 includes Ruby 3.4. Ruby 3.2 from AL2023 is not available. Amazon Linux follows the upstream support schedule and a support status of any Ruby version can always be checked on the [Ruby website](https://www.ruby-lang.org/en/). Amazon Linux namespaces the supported Ruby version so that future versions can be installed on the same system at the same time. Namespacing ensures that each Ruby installation is unique within the file system. This is achieved by renaming key directories and files based on the runtime version. The actual executable name will look like *ruby{MAJOR.MINOR}* (e.g., `ruby3.4`). Ruby 3.4 also provides the MRI (Matz's Ruby Interpreter) namespaced binary `ruby3.4-mri`, which refers to the standard C-based reference implementation of Ruby. However, only one Ruby version can be active at a time. This active version provides the default directories and file names, such as *ruby*, *gem*, or *bundle*, pointing them to the currently active runtime.

 This is achieved using the capabilities of the *alternatives* tool. It is important to remember that the default executable names are virtual and can change at any time when pointing to a different installed Ruby version. This flexibility enables software that uses *ruby* in the shebang to select the desired version when invoked. However, when a specific version of Ruby is required, persistence of the version can be achieved by calling the namespaced executable (e.g., `ruby3.4`), which will always use the specified version of the runtime. Additionally, the namespaced executables of the *gem* and *bundler* tools, such as `ruby3.4-gem` or `ruby3.4-bundler`, are always associated with the corresponding Ruby version, regardless of the currently active runtime.

 Ruby is distributed as several namespaced packages which begin with "`ruby{MAJOR.MINOR}`". These packages provide *ruby*, compatible versions of the *gem* and *bundler* tools, documentation, libraries, and more. For example, the core Ruby 3.4 runtime is provided by the `ruby3.4` package, which pulls in `ruby3.4-rubygems` (providing *gem*) and `ruby3.4-rubygem-bundler` (providing *bundle* and *bundler*) as dependencies.

 After installing a Ruby version, the entries for companion tools may show as null in the *alternatives* configuration. This can be verified by running `alternatives --display ruby`. If entries appear as null, they must be registered manually using `alternatives --install`. For example, to register all companion tools for Ruby 3.4:

```
sudo alternatives --install /usr/bin/gem gem /usr/bin/ruby3.4-gem 34
sudo alternatives --install /usr/bin/bundle bundle /usr/bin/ruby3.4-bundle 34
sudo alternatives --install /usr/bin/bundler bundler /usr/bin/ruby3.4-bundler 34
sudo alternatives --install /usr/bin/erb erb /usr/bin/ruby3.4-erb 34
sudo alternatives --install /usr/bin/racc racc /usr/bin/ruby3.4-racc 34
sudo alternatives --install /usr/bin/rdoc rdoc /usr/bin/ruby3.4-rdoc 34
sudo alternatives --install /usr/bin/ri ri /usr/bin/ruby3.4-ri 34
```

 The priority value (e.g., 34 for Ruby 3.4) should match the priority used in the main *ruby* alternative entry. Once registered, the companion tools will be managed automatically alongside the *ruby* alternative.

 The *alternatives* tool provides a single command for switching between installed Ruby versions. By default, *alternatives* is configured to be in auto mode, which uses priorities to determine the currently active Ruby version. However, you can activate any installed version at any time.

**Some useful examples of using *alternatives***

1. Check what *alternatives* is configured for

   ```
   alternatives --list
   ```

1. Check *ruby*'s current configuration

   ```
   alternatives --display ruby
   ```

1. Interactively change the Ruby version

   ```
   alternatives --config ruby
   ```

1. Switch to manual mode and select a specific version

   ```
   alternatives --set ruby /usr/bin/ruby{MAJOR.MINOR}
   ```

1. Switch back to auto version selection mode

   ```
   alternatives --auto ruby
   ```
