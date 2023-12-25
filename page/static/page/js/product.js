function showDropdown() {
    document.getElementById("myDropdown").classList.add('show');
    filterFunction();
}

// Hàm lọc các mục trong dropdown
function filterFunction() {
    let input, filter, dropdown, a, i, count = 0;
    input = document.getElementById("add_dvt");
    filter = input.value.toUpperCase();
    dropdown = document.getElementById("myDropdown");
    a = dropdown.getElementsByTagName("a");
    for (i = 0; i < a.length; i++) {
        txtValue = a[i].textContent || a[i].innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            a[i].style.display = "";
            count++;
        } else {
            a[i].style.display = "none";
        }
    }
    // Kiểm tra số lượng mục hiển thị và áp dụng thanh cuộn nếu cần
    dropdown.style.overflowY = count > 5 ? 'scroll' : 'hidden';
}

// Đóng dropdown khi click ra bên ngoài
window.onclick = function (event) {
    let txtValue;
    if (!event.target.matches('#add_dvt')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        let i;
        for (i = 0; i < dropdowns.length; i++) {
            const openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
        const add_dvt = document.getElementById("add_dvt").value;
        let input, dropdown, a, j;
        input = document.getElementById("add_dvt");
        filter = input.value.toUpperCase();
        dropdown = document.getElementById("myDropdown");
        a = dropdown.getElementsByTagName("a");
        for (j = 0; j < a.length; j++) {
            txtValue = a[j].textContent || a[j].innerText;
            if (add_dvt === txtValue) {
                document.getElementById("add_dvt").value = add_dvt;
                break;
            } else {
                document.getElementById("add_dvt").value = "";
            }
        }
    }
}

function currentDataTable() {
    let data_table = [];
    let table = document.getElementById("add-product");
    let tr = table.getElementsByTagName("tr");
    let add_product, add_size, add_dvt;
    for (let row = 0; row < tr.length; row++) {
        if (tr[row].style.display === "") {
            const td = tr[row].getElementsByTagName("td")[2];
            if (td) {
                add_product = td.getElementsByTagName("input")[0].value;
                add_size = td.getElementsByTagName("input")[1].value;
                add_dvt = td.getElementsByTagName("input")[2].value;
                if (add_product === "" || add_size === "" || add_dvt === "") {
                    continue;
                }
                data_table.push({
                    'add_product': add_product,
                    'add_size': add_size,
                    'add_dvt': add_dvt
                });
            }
        }
    }
    return data_table;
}

// Thêm sự kiện click cho mỗi mục trong dropdown
document.getElementById("myDropdown").addEventListener('click', function (e) {
    document.getElementById("add_dvt").value = e.target.innerText; // Thêm giá trị vào input
    document.getElementById("myDropdown").classList.remove('show'); // Ẩn dropdown
});

function click_add_product() {
    let check_add = false;
    const table = document.getElementById("add-product").getElementsByTagName('tbody')[0];
    const add_product = document.getElementById("add_product").value;
    const add_size = document.getElementById("add_size").value;
    const add_dvt = document.getElementById("add_dvt").value;
    if (add_product !== "" && add_size !== "" && add_dvt !== "") {
        const row = table.insertRow();
        row.innerHTML = '<td>' + add_product + '</td><td>' + add_size + '</td><td>' + add_dvt + '</td><td><a class="btn btn-danger" onclick="deleteRow(this)"> <i class="fa fa-trash"></i></a></td>';
        check_add = true;
    }
    if (check_add) {
        document.getElementById("add_product").value = "";
        document.getElementById("add_size").value = "";
        document.getElementById("add_dvt").value = "";
    }
}

function deleteRow(btn) {
    const row = btn.parentNode.parentNode;
    row.parentNode.removeChild(row);
}

function click_save_product() {
    console.log("click_save_product");
    let data_table = currentDataTable();
    let data = {
        'data_table': data_table
    }
    console.log(data);
    // $.ajax({
    //     url: '/page/save-product',
    //     type: 'POST',
    //     data: JSON.stringify(data),
    //     dataType: 'json',
    //     contentType: 'application/json; charset=utf-8',
    //     success: function (response) {
    //         if (response.status === 200) {
    //             alert(response.message);
    //             location.reload();
    //         } else {
    //             alert(response.message);
    //         }
    //     },
    //     error: function (response) {
    //         alert(response.message);
    //     }
    // });
}

