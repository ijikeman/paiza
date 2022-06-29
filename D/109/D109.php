<?php
/* ぞろ目判定 */
    $input_array = str_split(preg_replace("/ /", '', trim(fgets(STDIN))));
    if (count(array_unique($input_array)) == 1) {
        echo 'Yes';
    } else {
        echo 'No';
    }
?>
