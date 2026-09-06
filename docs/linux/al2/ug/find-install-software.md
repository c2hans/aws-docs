---
source_url: https://docs.aws.amazon.com/linux/al2/ug/find-install-software.html
---

# Find and install software packages on an AL2 instance
<a name="find-install-software"></a>

You can use a package management tool to find and install software packages. In Amazon Linux 2, the default software package management tool is YUM. In AL2023, the default software package management tool is DNF. For more information, see [Package management tool](https://docs.aws.amazon.com/linux/al2023/ug/package-management.html) in the *Amazon Linux 2023 User Guide*.

## Find software packages on an AL2 instance
<a name="find-software"></a>

You can use the **yum search** command to search the descriptions of packages that are available in your configured repositories. This is especially helpful if you don't know the exact name of the package you want to install. Simply append the keyword search to the command; for multiple word searches, wrap the search query with quotation marks.

```
[ec2-user ~]$ yum search "{{find}}"
```

The following is example output.

```
Loaded plugins: extras_suggestions, langpacks, priorities, update-motd
============================== N/S matched: find ===============================
findutils.x86_64 : The GNU versions of find utilities (find and xargs)
gedit-plugin-findinfiles.x86_64 : gedit findinfiles plugin
ocaml-findlib-devel.x86_64 : Development files for ocaml-findlib
perl-File-Find-Rule.noarch : Perl module implementing an alternative interface to File::Find
robotfindskitten.x86_64 : A game/zen simulation. You are robot. Your job is to find kitten.
mlocate.x86_64 : An utility for finding files by name
ocaml-findlib.x86_64 : Objective CAML package manager and build helper
perl-Devel-Cycle.noarch : Find memory cycles in objects
perl-Devel-EnforceEncapsulation.noarch : Find access violations to blessed objects
perl-File-Find-Rule-Perl.noarch : Common rules for searching for Perl things
perl-File-HomeDir.noarch : Find your home and other directories on any platform
perl-IPC-Cmd.noarch : Finding and running system commands made easy
perl-Perl-MinimumVersion.noarch : Find a minimum required version of perl for Perl code
texlive-xesearch.noarch : A string finder for XeTeX
valgrind.x86_64 : Tool for finding memory management bugs in programs
valgrind.i686 : Tool for finding memory management bugs in programs
```

Multiple word search queries in quotation marks only return results that match the exact query. If you don't see the expected package, simplify your search to one keyword and then scan the results. You can also try keyword synonyms to broaden your search.

For more information about packages for AL2, see the following:
+ [AL2 Extras Library](al2-extras.md)
+ [Package repository](ec2.md#package-repository)

## Install software packages on an AL2 instance
<a name="install-software"></a>

In AL2, the yum package management tool searches all of your enabled repositories for different software packages and handles any dependencies in the software installation process. For information about installing software packages in AL2023, see [Managing packages and operating system updates](https://docs.aws.amazon.com/linux/al2023/ug/managing-repos-os-updates.html) in the *Amazon Linux 2023 User Guide*.

**To install a package from a repository**
Use the **yum install {{package}}** command, replacing {{package}} with the name of the software to install. For example, to install the **links** text-based web browser, enter the following command.

```
[ec2-user ~]$ sudo yum install links
```

**To install RPM package files that you have downloaded**
You can also use **yum install** to install RPM package files that you have downloaded from the internet. To do this, append the path name of an RPM file to the installation command instead of a repository package name.

```
[ec2-user ~]$ sudo yum install {{my-package}}.rpm
```

**To list installed packages**
To view a list of installed packages on your instance, use the following command.

```
[ec2-user ~]$ yum list installed
```
