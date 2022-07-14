<?php
/**
 * Get 1 Line from STDIN
 *
 * @method get()
 * @return
 *   - string or FALSE
 */
class Stdin {
    static function get() {
        if ($result = fgets(STDIN)) {
            $result = trim($result);
            return $result;
        }
        return FALSE;
    }
}

/** 
 * Get Multi Line from STDIN
 *
 * @method get()
 * @param int $max_num: 最大取得可能行
 * @return
 *   - array()
 */
class Stdins {
    static function get($max_num) {
        $list = array();
        for ($i=0; $i < $max_num; $i++) {
            $result = Stdin::get();
            if ($result == FALSE) {
                break;
            } else {
                array_push($list, $result);
            }
        }
        return $list;
    }
}

/**
 * Get 1 Line from File
 *
 * @method get()
 * @return
 *   - string or FALSE
 */
class GetLineFromFile {
    static function get($fp) {
        if ($result = fgets($fp)) {
            $result = trim($result);
            return $result;
        }
        return FALSE;
    }
}

/** 
 * Get Multi Line from File
 *
 * @method get()
 * @param int $filename: ファイル名
 * @param int $max_num: 最大取得可能行
 * @return
 *   - array()
 */
class GetLinesFromFile {
    static function get($fp, $max_num) {
        $list = array();
        for ($i=0; $i < $max_num; $i++) {
            $result = GetLineFromfile::get($fp);
            if ($result == FALSE) {
                break;
            } else {
                array_push($list, $result);
            }
        }
        return $list;
    }
}

/**
 * Set Data of Paiza-format to Array
 *
 * @method setData()
 * @method getData()
 * @param int $max_num
 */
class PaizaData {
    function __construct() {
        $this->data = array();
    }
    function setData($data) {
        $this->data[] = $data;
    }
    function getData($array_num) {
        return $this->data[($array_num-1)];
    }
}

/**
 * 判定した数値を返す
 * [条件]
 * -- 全ての行で判定する -- 
 * 前がなしで次が. 0 ok
 * 前が.で次が. 0 ok
 * 前が#で次が. +1 ok
 * 前がなしで次が# +1 ok
 * 前が.で次が# +1 ok
 * 前が#で次が# 0 ok
 * -- 最初の行と最後の行は判定する
 * 最初/最終行.なら 0 ok
 * 最初/最終行#なら +1 ok
 * -- 最初の行以外は判定する
 * 前の行がなしで.0 ok
 * 前の行が.で. 0 ok
 * 前の行が#で. +1 ok

 * 前の行がなしで# +1 ok
 * 前の行が.で# +1 ok
 * 前の行が#で # 0 ok
 * --判定条件終了 --
 */
class Judge {
    public $SCORE = 0;
    function judge($uppper_data=NULL, $before_data=NULL, $current_data=NULL, $current_line_number, $max_line_number) {
        switch($current_data) {
            case '.':
                switch ($before_data) {
                    case NULL:
                        $this->SCORE += 0;
                        break;
                    case '.':
                        $this->SCORE += 0;
                        break;
                    case '#':
                        $this->SCORE++;
                        break;
                }
                switch ($uppper_data) {
                    case NULL:
                        $this->SCORE += 0;
                        break;
                    case '.':
                        $this->SCORE += 0;
                        break;
                    case '#':
                        $this->SCORE++;
                        break;
                }
                break;
            case '#':
                switch ($before_data) {
                    case NULL:
                        $this->SCORE++;
                        break;
                    case '.':
                        $this->SCORE++;
                        break;
                    case '#':
                        $this->SCORE += 0;
                        break;
                }
                switch ($uppper_data) {
                    case NULL:
                        $this->SCORE++;
                        $this->SCORE++; // first line
                        break;
                    case '.':
                        $this->SCORE++;
                        break;
                    case '#':
                        $this->SCORE += 0;
                        break;
                }
                if ($current_line_number == $max_line_number) { // last line
                    $this->SCORE++;
                }
                break;
        }
    }
}

/**
 *  main
 */
$paiza = new PaizaData();

/**
 * Data Input
 */
/* STDIN用(on Paiza) */
//list($max_tate, $max_yoko) = explode(' ', trim(Stdin::get(1))); // parse First Line
//$paiza->setData(Stdins::get($max_tate)); // set Second Data
/* local Debug用 */
$fp = fopen('./data1.txt', 'r');
list($max_tate, $max_yoko) = explode(' ', trim(GetLineFromFile::get($fp))); // parse First Line
$paiza->setData(GetLinesFromFile::get($fp, $max_tate)); // set Second Data
// print_r($paiza->getData(1));
/**
 * End Data Input
 */


$split_data = array();
$judge = new Judge();
$before_data = $uppper_data = $current_data = NULL;
for($i = 0; $i < count($paiza->getData(1)); $i++) {
    $current_line_number = 0;
    foreach (str_split($paiza->getData(1)[$i]) as $current_data) { // コンテンツデータを１文字ずつ分割し判定
        $judge->judge($uppper_data, $before_data, $current_data, $current_line_number, $max_tate);
    }
}


// .##.
// .##.
// .##.
// .##.
// 0211 4
// 0101 2
// 0101 2
// 0211 4
//=12

// ..#.
// ..#.
// ###.
// ..#.
// 0021
// 0011
// 2101
// 1121
// =14
?>
