#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	net-http-pipeline
Summary:	An HTTP/1.1 pipelining implementation atop Net::HTTP
Name:		ruby-%{pkgname}
Version:	1.0.1
Release:	1
License:	GPL v2+ or Ruby
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	50f3b868dab4ef1359d0777cdacda2e1
URL:		http://docs.seattlerb.org/net-http-pipeline
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-hoe < 3
BuildRequires:	ruby-hoe >= 2.16
BuildRequires:	ruby-minitest < 3
BuildRequires:	ruby-minitest >= 2.11
BuildRequires:	ruby-rdoc < 4
BuildRequires:	ruby-rdoc >= 3.10
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An HTTP/1.1 pipelining implementation atop Net::HTTP. A pipelined
connection sends multiple requests to the HTTP server without waiting
for the responses. The server will respond in-order.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/net/http/pipeline.rb
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
