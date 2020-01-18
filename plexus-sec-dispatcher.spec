Name:           plexus-sec-dispatcher
Version:        1.4
Release:        13%{?dist}
Summary:        Plexus Security Dispatcher Component

License:        ASL 2.0
URL:            http://spice.sonatype.org
#svn export http://svn.sonatype.org/spice/tags/plexus-sec-dispatcher-1.4/
#tar jcf plexus-sec-dispatcher-1.4.tar.bz2 plexus-sec-dispatcher-1.4/
Source0:        %{name}-%{version}.tar.bz2

BuildArch: noarch

BuildRequires: java-devel >= 1:1.6.0
BuildRequires: maven-local
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: plexus-utils
BuildRequires: plexus-cipher
BuildRequires: plexus-containers-component-metadata
BuildRequires: junit
BuildRequires: forge-parent
BuildRequires: spice-parent
BuildRequires: maven-surefire-provider-junit

%description
Plexus Security Dispatcher Component

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.


%prep
%setup -q

# annotations are not available for Java 1.4, remove definition
# pom_remove_plugin doesn't handle newline in artifactId gracefully
# https://bugzilla.redhat.com/show_bug.cgi?id=998463
sed -i '/maven-compiler-plugin/ {
    N; # Add next line to buffer
    s:maven-compiler-plugin\n *:maven-compiler-plugin:
    }' pom.xml
%pom_remove_plugin :maven-compiler-plugin

# use plexus-component-metadata instead of old plugin
%pom_remove_plugin :plexus-maven-plugin
%pom_add_plugin org.codehaus.plexus:plexus-component-metadata pom.xml "
         <executions>
           <execution>
             <goals>
              <goal>generate-metadata</goal>
             </goals>
           </execution>
         </executions>
"

%mvn_file : plexus/%{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%files javadoc -f .mfiles-javadoc

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.4-13
- Mass rebuild 2013-12-27

* Mon Aug 19 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4-12
- Migrate away from mvn-rpmbuild (#997450)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-11
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Wed Apr 10 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-10
- Remove unneeded BR: plexus-container-default

* Thu Feb  7 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-9
- Remove unneeded R: spice-parent, resolves: rhbz#908584
- Remove RPM bug workaround

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.4-8
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 22 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4-6
- Replace plexus-maven-plugin with plexus-component-metadata

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 23 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4-4
- Fixes according to new guidelines
- Add spice-parent to Requires
- Versionless jars & javadocs
- Use maven3 to build

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jun 04 2010 Hui Wang <huwang@redhat.com> - 1.4-2
- Fixed url

* Fri May 21 2010 Hui Wang <huwang@redhat.com> - 1.4-1
- Initial version of the package
