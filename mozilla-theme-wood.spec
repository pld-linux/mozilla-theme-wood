%define		_realname	wood
%define		_mozver		1.2.1
Summary:	Wooden theme based on LittleMozilla
Summary(pl):	Drewniany motyw bazuj±cy na LittleMozilla
Name:		mozilla-theme-wood
Version:	1.2
%define	_fver	%(echo %{version} | tr -d .)
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.uk1.mozdev.org/rsync/themes/themes/%{_realname}_%{_fver}.jar
# Source0-md5:	787b7c7b9576c0a4136f06047f68b4ee
Source1:	%{_realname}-installed-chrome.txt
URL:		http://themes.mozdev.org/themes/wood.html
Requires(post,postun):	textutils
Requires:	mozilla >= %{_mozver}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_chromedir	%{_libdir}/mozilla/chrome

%description
Theme made with care for details. All browser elements are made of
wood. Small buttons and toolbars leave big workspace.

%description -l pl
Motyw wykonany z wielkim wyczuciem i dba³o¶ci± o szczegó³y. Wszystkie
elementy przegl±darki s± wykonane drewna. Niewielkie przyciski i paski
narzêdziowe pozwalaj± na maksymalne wykorzystanie przestrzeni roboczej.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install %{SOURCE0} $RPM_BUILD_ROOT%{_chromedir}/%{_realname}.jar
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%postun
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
