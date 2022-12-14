var $college_select = $( '#college_select' ),
$course_select = $( '#course_select' ),
$options = $course_select.find( 'option' );

$college_select.on( 'change', function() {
$course_select.html( $options.filter( '[value="' + this.value + '"]' ) );
} ).trigger( 'change' );