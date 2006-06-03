#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	AI
%define	pnam	NNEasy
Summary:	AI::NNEasy - Define, learn and use easy Neural Networks of different types
Summary(pl):	AI::NNEasy - definiowanie, uczenie i u¿ywanie ³atwych sieci neuronowych
Name:		perl-AI-NNEasy
Version:	0.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/G/GM/GMPASSOS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	110f3b4b0e0f2575ef4f8dd3dfc8a0e4
BuildRequires:	perl-Class-HPLOO >= 0.21
BuildRequires:	perl-Inline >= 0.44
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The main purpose of this module is to create easy Neural Networks with
Perl.

The module was designed to can be extended to multiple network types,
learning algorithms and activation functions. This architecture was
1st based in the module AI::NNFlex, than I have rewrited it to fix
some serialization bugs, and have otimized the code and added some XS
functions to get speed in the learning process. Finally I have added
an intuitive inteface to create and use the NN, and added a winner
algorithm to the output.

I have writed this module because after test different NN module on
Perl I can't find one that is portable through Linux and Windows, easy
to use and the most important, one that really works in a real
problem.

With this module you don't need to learn much about NN to be able to
construct one, you just define the construction of the NN, learn your
set of inputs, and use it.

%description -l pl
G³ównym celem tego modu³u jest tworzenie ³atwych sieci neuronowych
(Neural Networks, w skrócie NN) w Perlu.

Modu³ zosta³ zaprojektowany tak, aby mo¿na by³o go rozszerzaæ do wielu
rodzajów sieci, algorytmów ucz±cych czy funkcji aktywacyjnych.
Architektura ta zosta³a najpierw oparta na module AI::NNFlex,
nastêpnie przepisana w celu poprawienia b³êdów serializacji,
zoptymalizowana wraz z dodaniem funkcji XS w celu poprawienia
szybko¶ci w procesie uczenia. Ostatecznie dodano intuicyjny interfejs
do tworzenia i u¿ywania sieci neuronowych oraz dodano algorytm
zwyciêzcy na wyj¶ciu.

Modu³ ten zosta³ napisany poniewa¿ po testach ró¿nych modu³ów do sieci
neuronowych autor nie znalaz³ ¿adnego wystarczaj±co przeno¶nego miêdzy
Linuksem a Windows, ³atwego w u¿yciu i co najwa¿niejsze naprawdê
dzia³aj±cego przy rzeczywistych problemach.

Przy u¿yciu tego modu³u nie trzeba uczyæ siê zbyt wiele o sieciach
neuronowych aby móc takow± skonstruowaæ, wystarczy zdefiniowaæ
konstrukcjê sieci, nauczyæ zbiór wej¶æ i u¿ywaæ.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a samples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/AI/*.*
%{perl_vendorarch}/AI/NNEasy
%dir %{perl_vendorarch}/auto/AI/NNEasy/NN
%dir %{perl_vendorarch}/auto/AI/NNEasy/NN/[bf]*
%attr(755,root,root) %{perl_vendorarch}/auto/AI/NNEasy/*.so
%attr(755,root,root) %{perl_vendorarch}/auto/AI/NNEasy/*/*.so
%attr(755,root,root) %{perl_vendorarch}/auto/AI/NNEasy/*/*/*.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
