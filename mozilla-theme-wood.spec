Summary:	Wooden theme based on LittleMozilla
Summary(pl):	Drewniany temat bazuj�cy na LittleMozilla
Name:		mozilla-theme-wood
Version:	1.0
%define		_realname	wood
%define		_fver	%(echo %{version} | tr -d .)
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.mozdev.org/themes/%{_realname}_%{_fver}.jar
Source1:	%{_realname}-installed-chrome.txt
URL:		http://themes.mozdev.org/skins/pinball.html
BuildArch:	noarch
Requires:	mozilla >= 1.0-7
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_libdir}/mozilla/chrome

%description
Theme made with care for details. All browser elements are made of
wood. Small buttons and toolbars leave big workspace.

%description -l pl
Temat wykonany z wielkim wyczuciem i dba�o�ci� o szczeg�y. Wszystkie
elementy przegl�darki s� wykonane drewna. Niewielkie przyciski i paski
narz�dziowe pozwalaj� na maksymalne wykorzystanie przestrzeni roboczej.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install %{SOURCE0} $RPM_BUILD_ROOT%{_chromedir}/%{_realname}.jar
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean 
rm -rf $RPM_BUILD_ROOT

%post 
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%postun
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt