<?php
/**
 * Created by PhpStorm.
 * User: Administrator
 * Date: 2017/9/24
 * Time: 0:34
 */
$dir=$_POST['dir'];
$act=$_POST['act'];
$style=$_POST['style'];
$year=$_POST['year'];
$focus=$_POST['focus'];

$act=explode(',',trim($act,','));
$style=explode(',',trim($style,','));

print_r($_POST);

