function isMobileDevice() {
    return (typeof window.orientation !== "undefined") || (navigator.userAgent.indexOf('IEMobile') !== -1);
};

if( isMobileDevice() ) {
    window.location = "{% url 'portfolio:portfolio' %}";
}