Summary:	Basic single-file add-ons for editing C code
Summary(pl):	Basic single-file add-ons for editing C code
Name:		xemacs-c-support-pkg
%define 	srcname	c-support
Version:	1.14
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
URL:		http://www.xemacs.org/
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-cc-mode-pkg
Requires:	xemacs-base-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl 

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

gzip -9nf lisp/c-support/ChangeLog 

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/c-support/ChangeLog.gz 
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.elc
