function validarFormulario() {

    let txtSpa = document.getElementById("txtSpa").value;
    let txtNombre = document.getElementById("txtNombre").value;
    let txtTiempo = document.getElementById("txtTiempo").value;
    let txtPrecio = document.getElementById("txtPrecio").value;
    let txtFoto = document.getElementById("txtFoto").value;

    /*if (txtSpa == null || txtSpa.length == 0 || /^\s+$/.test(txtSpa) || !isNaN(txtSpa) || /\d+/g.test(txtSpa))
        alert('ERROR: El campo "Spa" no debe ir vacío, lleno de solamente espacios en blanco ni debe contener números');*/
    if (txtNombre == null || txtNombre.length == 0 || /^\s+$/.test(txtNombre))
        alert('ERROR: El campo "Servicio" no debe ir vacío o lleno de solamente espacios en blanco');
    if (txtTiempo == null || txtTiempo.length == 0 || /^\s+$/.test(txtTiempo))
        alert('ERROR: El campo "Tiempo" no debe ir vacío o lleno de solamente espacios en blanco');
    if (txtPrecio == null || txtPrecio.length == 0 || /^\s+$/.test(txtPrecio))
        alert('ERROR: El campo "Precio" no debe ir vacío o lleno de solamente espacios en blanco');
    if (isNaN(txtPrecio))
        alert('ERROR: El campo "Precio" debe contener números');
    if (txtFoto.files.length == 0) {
        alert("Please attach your CV");

    }
}